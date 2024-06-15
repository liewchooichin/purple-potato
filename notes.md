# My Notes

## Using `uvicorn` with Django
To use [uvicorn with django](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/uvicorn/):

```python -m uvicorn myproject.asgi:application```

## Configure database information as environment variables
az webapp config appsettings set --settings DB_SERVER="<azure-sql-server-name>.database.windows.net" DB_NAME="<db-name>" DB_USER="<db-user-id>" DB_PASSWORD="<db-password>"

## Create a web app and deploy the code
az webapp up -g <MyResourceGroup> -l <location> -p <azure-sql-db-django-plan> --sku B1 -n <azure-sql-db-django-api> -r 'PYTHON:3.9'

