import re

from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountUpdateParameters
from azure.mgmt.subscription import SubscriptionClient

from auth import CREDENTIALS
from database import SessionLocal
from models import StorageAccounts
from schemas import StorageCreate

db = SessionLocal()
accounts = {}


def get_storage():
    data = db.query(StorageAccounts).all()
    return data


def get_latest_storage():
    data = db.execute(
        'SELECT DISTINCT ON (name) * FROM "StorageAccount" ORDER BY NAME DESC;'
    )
    print("Storage data refreshed!")
    return data


def delete_storage(data):
    for i in data:
        db.query(StorageAccounts).filter(StorageAccounts.name == i).delete()
        print(f"Deleted Storage Account - {i}")


def create_storage():
    accounts = storage_list()
    db_storage = {i.name for i in get_storage()}
    az_storage = set()

    # need to add some validation to make sure if matches the pydantic schema. not sure how to do this yet.
    for account in accounts:
        db_item = StorageAccounts(
            name=account.name,
            public=account.allow_blob_public_access,
            tls=account.minimum_tls_version,
            https=account.enable_https_traffic_only,
            subscription=re.search(
                "subscriptions/(.*)/resourceGroups", account.id
            ).group(1),
            resource_group=re.search("resourceGroups/(.*)/providers", account.id).group(
                1
            ),
        )  # this data will be the storage account information at some point
        # if account.name not in db_storage():
        #     delete_storage():
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        az_storage.add(account.name)
    storage_diff = db_storage.difference(az_storage)
    if storage_diff:
        delete_storage(storage_diff)  # what's in the db that isn't on azure. bye bye.


def list_subscriptions():
    client = SubscriptionClient(CREDENTIALS)
    # ignore disabled subscriptions
    subs = [
        sub.subscription_id
        for sub in client.subscriptions.list()
        if sub.state.value == "Enabled"
    ]

    return subs


# change this to refresh storage and pass output into create_storage()
def storage_list():
    subs = list_subscriptions()
    for sub in subs:
        storage_client = StorageManagementClient(CREDENTIALS, sub)
        storage_accounts = storage_client.storage_accounts.list()
        for account in storage_accounts:
            yield account


def get_storage_properties(storage_id):
    record = db.query(StorageAccounts).filter(StorageAccounts.name == storage_id).all()
    return record


def storage_remediations(storage_id, action):
    properties = get_storage_properties(storage_id)
    storage_client = StorageManagementClient(CREDENTIALS, properties.subscription)
    if action == "TLS":
        storage_client.storage_accounts.update(
            properties.resource_group,
            properties.name,
            StorageAccountUpdateParameters(minimum_tls_version="TLS1_2"),
        )
    elif action == "HTTPS":
        storage_client.storage_accounts.update(
            properties.resource_group,
            properties.name,
            StorageAccountUpdateParameters(enable_https_traffic_only=True),
        )
    else:
        storage_client.storage_accounts.update(
            properties.resource_group,
            properties.name,
            StorageAccountUpdateParameters(allow_blob_public_access=False),
        )
    create_storage()
