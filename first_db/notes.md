# Steps

## Login using az login --use-device-code

## In the web app, set to Identity--System Assigned.

## In the web app, set the environment variables:

AZURE_SQL_CONNECTIONSTRING="<connection-string>"

Driver={ODBC Driver 18 for SQL Server};Server=tcp:<database-server-name>.database.windows.net,1433;Database=<database-name>;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30

## Use webapp to database
Use the Query Editor to add the web app as a user of the database:

CREATE USER blueberry201 FROM EXTERNAL PROVIDER
ALTER ROLE db_datareader ADD MEMBER blueberry201
ALTER ROLE db_datawriter ADD MEMBER blueberry201

## Create the startup file

The startup file has only one line:

```gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app```

Go to https://learn.microsoft.com/en-us/azure/developer/python/configure-python-web-app-on-app-service

## webapp **config** set
az webapp config set --resource-group DefaultResourceGroup-SEA --name blueberry201 --start-up start.shaz webapp config set --resource-group DefaultResourceGroup-SEA --name blueberry201 --start-up start.sh

