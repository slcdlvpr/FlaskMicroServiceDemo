from azure.cosmos import exceptions, CosmosClient, PartitionKey
import uuid

class repository(object):
    def __init__(self, connection, key, containerid, databasename):
        self.connection = connection
        self.key = key
        self.conatinerid = containerid
        self.databasename = databasename
        

    def updateLocation(self, serialId, location, datetime):
        client = CosmosClient(self.connection, self.key)
        database_name = self.databasename
        database = client.create_database_if_not_exists(id=database_name)
        container = database.create_container_if_not_exists(
        id=self.conatinerid, 
        partition_key=PartitionKey(path="/deviceid"),
        offer_throughput=400
        )  
        uid =  uuid.uuid4()
        itemtelemetry = {
        'id':  str(uid), 
        'deviceid': serialId,
        'location' : location,
        'datetime':datetime
        }
        container.create_item(body=itemtelemetry)
        



