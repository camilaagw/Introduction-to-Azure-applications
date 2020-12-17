# Azure Storage

Azure Storage features:
- Automated backup and recovery
- Data replication  at multiple data centers worldwide
- Data analytics support
- Data encryption for added security
- Support for multiple data types
- Scale up or scale out 

Some of the Azure Storage options are:

- Azure SQL Server and SQL Database
- Azure Blob Storage
- Azure CosmosDB
- Disk Storage
- Azure Data Lake Storage
- HPC Cache

The two main services covered in this lesson are:
 - Azure SQL Databases 
 - Blob Storage
 
## Azure SQL Databases

- Used for structured, relational data
- A SQL server needs to be created to hold a database (You can hold multiple SQL databases under a single SQL server)
- Azure SQL databases do not have a free tier option 

## Blob Storage
Blob storage is done inside **Azure Storage Accounts**. An Azure storage account:
- Can hold Files or Blobs
- Provides a unique namespace in Azure for your data
- Can contain multiple containers within them to organize different files
- Offer different storage tiers: Hot, Cold and Archive
- Offer a rule-based policy you can use to transition your data between these tiers


__Blob (Binary Large Object): Data type that can store unstructured (binary) data. Generally used to store images or videos.__