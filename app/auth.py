import os

# Azure stuff
from azure.common.credentials import ServicePrincipalCredentials

# Get environment variables
client_id = os.getenv("CLIENT_ID", "NA")
client_secret = os.getenv("CLIENT_SECRET", "NA")
tenant_id = os.getenv("TENANT_ID", "NA")

CREDENTIALS = ServicePrincipalCredentials(
    client_id=client_id, secret=client_secret, tenant=tenant_id,
)
