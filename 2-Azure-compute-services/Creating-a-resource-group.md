# Creating a resource group

Login using `az login`, and run:
```markdown
az group create --name <resource-grup-name> --location <my-location>
```
Example: `az group create --name resource-group-west --location westus2`

Note: To see list of all locations, you can run `az account list-locations -o table`

## How to choose a region for a compute service?
There are three criteria:
- Service availability - Some services may not be available in a particular region.
- Performance - Latency determines network service performance; are you creating resources for yourself or your end user?
- Cost - Costs of services vary by region. If latency isn’t an issue, you might want to deploy your services in the cheapest region.