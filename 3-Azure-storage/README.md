# Lesson 3: Azure Storage

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

Note that Azure SQL databases do not have a free tier option. 

## Blob Storage
Blob storage is done inside **Azure Storage Accounts**. An Azure storage account:
- Can hold Files, disks, or Blobs
- Provides a unique namespace in Azure for your data
- Can contain multiple containers within them to organize different files
- Offer different storage tiers:
    - Hot: Used for storing frequently accessed data
    - Cold: Used for storing infrequently accessed data and stored for at least 30 days
    - Archive: Used for storing data that will be rarely accessed and stored for at least 180 days.
     Access time latency may be very high
- Offer a rule-based policy  to transition your data between these tiers

__Blob (Binary Large Object): Data type that can store unstructured (binary) data. Generally used to store images or videos.__

Blob Storage is ideal for:

- Serving images or documents directly to a browser.
- Storing files for distributed access.
- Streaming video and audio.
- Storing data for backup and restore, disaster recovery, and archiving.
- Storing data for analysis by an on-premises or Azure-hosted service.
- Storing up to 8 TB of data for virtual machines

## Azure CosmosDB
Azure's non-relational database service, capable of using different non-relational databases like MongoDB and Cassandra.

## HPC Cache
A cache used for faster access to certain data used for high performance compute, while leaving the rest of large datasets in other storage options.