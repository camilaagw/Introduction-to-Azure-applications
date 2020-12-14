# Deploying an App Service Web App

## Creating the App Service

Login using `az login`.

From the `web` directory, run:

```
az webapp up \
 --resource-group <resource-group-name> \
 --name <your_app_name> \
 --sku F1 \
 --verbose
```
You will receive a json response with the URL of the deployed app.

To update your app, make changes to your code and then run it, you can use:
```
az webapp up \
 --name <your_app_name> \
 --verbose
```

## Cleanup


Delete a resource group:
```
az group delete -n <resource-group-name>
```

Delete an App Service:
```
az webapp delete \
    --name <your_app_name> \
    --resource-group <resource-group-name>
```

Delete an App Service plan:
```
az appservice plan delete \
    --name [App Service Plan Name] \
    --resource-group <resource-group-name>
```