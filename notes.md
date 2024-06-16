# My Notes

## Using `uvicorn` with Django

To use [uvicorn with django](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/uvicorn/):

```python -m uvicorn myproject.asgi:application```

## Configure database information as environment variables

az webapp config appsettings set --settings DB_SERVER="<azure-sql-server-name>.database.windows.net" DB_NAME="<db-name>" DB_USER="<db-user-id>" DB_PASSWORD="<db-password>"

## config setup

Currently the decouple.config() is set to local development mode. When deploying to Web App, comment out the corresponding config in the `settings.py`.

## django app 

Username: codespace
Password: my gh

## `simple_db.py`

This is a sample of connection to the SQL using pyodbc.

## `DISABLE_COLLECTSTATIC`

Currently, the Web App environment variable is set to `DISABLE_COLLECTATIC=false`. It may have to change depending on the situations.
