# Create an Azure Blob Storage from the CLI

First, create the storage account:
```markdown
az storage account create \
 --name helloworld12345 \
 --resource-group resource-group-west \
 --location westus2
```
Note 1: As there a not other options passed, the storage will default to general purpose V2.  
Note 2: The tier cannot be set from the CLI, so it will default to hot.

Create the container passing the name of the storage account:
```markdown
az storage container create \
 --account-name helloworld12345 \
 --name images \
 --auth-mode login \
 --public-access container
```

## Uploading files
Files can be uploaded directly from the Azure Portal or by connecting the storage account to an app.

For this, in Python there is the Azure Storage Blob Library. You can install it via pip: `pip install azure-storage-blob`.

Uploading a blob:
```markdown
from azure.storage.blob import BlobServiceClient

blob_container = app.config['BLOB_CONTAINER']
storage_url = "https://{}.blob.core.windows.net/".format(app.config['BLOB_ACCOUNT'])
blob_service = BlobServiceClient(account_url=storage_url, credential=app.config['BLOB_STORAGE_KEY'])

blob_client = blob_service.get_blob_client(container=blob_container, blob=filename)
blob_client.upload_blob(file)
```

Deleting a blob:
```markdown
blob_client = blob_service.get_blob_client(container=blob_container, blob=filename)
blob_client.delete_blob()
```