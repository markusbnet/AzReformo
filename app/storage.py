from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.subscription import SubscriptionClient

from auth import CREDENTIALS

accounts = []


def list_subscriptions():
    client = SubscriptionClient(CREDENTIALS)
    # ignore disabled subscriptions
    subs = [
        sub.subscription_id
        for sub in client.subscriptions.list()
        if sub.state.value == "Enabled"
    ]

    return subs


# we need to think about pulling this data at the beginning of the run and storing it somewhere. then run a background job to refresh it every x minutes.
def storage_list():
    subs = list_subscriptions()
    for sub in subs:
        storage_client = StorageManagementClient(CREDENTIALS, sub)
        storage_accounts = storage_client.storage_accounts.list()
        for account in storage_accounts:
            accounts.append(account)
