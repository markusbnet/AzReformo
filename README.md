# AzReformo
Fixing all those bad things someone did to your Azure tenant

## Running AzReformo
1. Export an Azure Client ID, Client Secret and Tenant ID
``` 
export CLIENT_ID=""
export CLIENT_SECRET=""
export TENANT_ID=""
```
2. Setup your virtual environment
‘‘‘virtualenv -p python3 .venv‘‘‘
3. source .venv/bin/activate
4. pip install -r requirements.txt
5. uvicorn main:app --reload


## Setting up for developent
1. Setup your virtual environment
‘‘‘virtualenv -p python3 .venv‘‘‘
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. uvicorn main:app --reload