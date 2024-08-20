
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://atpl:atpl@atlascluster.bwijqfd.mongodb.net/?appName=AtlasCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
#getting database, cilent is a dict object and we are passing key gw2024pds    
db = client['gw2024pds']  # use database in mysql

#getting list of collections from database
collections = db.list_collection_names()


#printing list of collections
for collection in collections:
    print(collection)
    
#getting documents from collections
documents = db['users'].find()

# printing documents in user collection
for document in documents:
    print(document)