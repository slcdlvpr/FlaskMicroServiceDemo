import configparser
import os
from Repository.repository import repository

class cosmosdbservice(object):
    """service that handles all interaction with cosmosdb"""
    def __init__(self):
        
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, 'config.cfg')

        config = configparser.ConfigParser()
        config.readfp(open(filename))
        self.databasename = config.get('CosmosdbConfig', 'databasename')
        self.containerid = config.get('CosmosdbConfig', 'containerid')
        self.endpoint = config.get('CosmosdbConfig', 'endpoint')
        self.key = config.get('CosmosdbConfig', 'key')
       
    
    def updateLocation(self, serialId, coordinates,datetime):
        rep = repository (self.endpoint,self.key,self.containerid,self.databasename)
        rep.updateLocation(serialId, coordinates,datetime)

