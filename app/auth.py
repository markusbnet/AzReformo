import os

# Azure stuff
from azure.common.credentials import ServicePrincipalCredentials
from config import settings

CREDENTIALS = ServicePrincipalCredentials(
    client_id=settings.client_id, secret=settings.secret_id, tenant=settings.tenant_id,
)
