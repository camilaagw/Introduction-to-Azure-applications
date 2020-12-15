# Create an Azure SQL database

Create SQL Server:
```markdown
az sql server create \
--admin-user udacityadmin \
--admin-password p@ssword1234 \
--name hello-world-server \
--resource-group resource-group-west \
--location westus2 \
--enable-public-network true \
--verbose
```

Create Firewall rule to allow Allow Azure services and resources to access the server:
```markdown
az sql server firewall-rule create \
-g resource-group-west \
-s hello-world-server \
-n azureaccess \
--start-ip-address 0.0.0.0 \
--end-ip-address 0.0.0.0 \
--verbose
```

Create a Firewall rule for the client:
```markdown
az sql server firewall-rule create \
-g resource-group-west \
-s hello-world-server \
-n clientip \
--start-ip-address <PUBLIC-IP-ADDRESS> \
--end-ip-address <PUBLIC_IP_ADDRESS> \
--verbose
```

Create a SQl database:
```markdown
az sql db create \
--name hello-world-db \
--resource-group resource-group-west \
--server hello-world-server \
--tier Basic \
--verbose
```

## Cleanup

Delete DB:
```markdown
az sql db delete \
--name hello-world-db \
--resource-group resource-group-west \
--server hello-world-server \
--verbose
```

Delete SQL Server:
```markdown
az sql server delete \
--name hello-world-server \
--resource-group resource-group-west \
--verbose
```

