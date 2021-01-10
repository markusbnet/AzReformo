import os

# Azure stuff
from azure.common.credentials import ServicePrincipalCredentials
from config import settings

CREDENTIALS = ServicePrincipalCredentials(
    client_id=settings.client_id,
    secret=settings.client_secret,
    tenant=settings.tenant_id,
)
