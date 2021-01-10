# AzReformo
Fixing all those bad things someone did to your Azure tenant

## Running AzReformo
1. ```docker run -d -p 80:80 --env TENANT_ID="" --env CLIENT_ID="" --env CLIENT_SECRET="" azreformo```

## Setting up for development
1. Create a .env file with the following set (this will not be commited).
```
TENANT_ID=""
CLIENT_ID=""
CLIENT_SECRET=""
POSTGRES_PASSWORD=""
```
2. Run
```
docker-compose up
```

### Postgres
1. Defaults
    - Username = postgres
    - Password = <set in .env file>
    - Database = postgres
2. Access adminer through localhost:8080
