# Deploying an App Service Web App

## Creating and deploying the App Service from the CLI

Login using `az login`.

From the `web` directory (or your application directory), run:

```
az webapp up \
 --resource-group <resource-group-name> \
 --name <your-app-name> \
 --sku F1 \
 --verbose
```
Note that `<your-app-name>` needs to be a unique name to Azure as a whole and not just your Azure account.

If the request is successful will receive a json response with the URL of the deployed app.

To update your app, make changes to your code and then run it, you can use:
```
az webapp up \
 --name <your_app_name> \
 --verbose
```

## Deploying an App Service from a GitHub repository

Once your app was created, in the Azure Portal:

1. Go to Deployment Center
2. Choose GitHub
3. Choose org and repo
4. Go through the prompts; deployment takes a few minutes
5. Go to URL of web app and should see the app deployed

Sources: https://youtu.be/C4B4Ebchf0U, https://youtu.be/bpME7sOhPNg

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