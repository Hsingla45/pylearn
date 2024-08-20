from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# CREATING THIS CLASS AS IT HELPS US TO DO OPEARTIONS WITH MONGODB

class MongoDBHelper:
    def __init__(self, collection="users"):
        uri = "mongodb+srv://atpl:atpl@atlascluster.bwijqfd.mongodb.net/?appName=AtlasCluster"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
    
    
    
        self.db = client['gw2024pds'] # selectiong database


        self.collection = self.db[collection] #collection is list of dict in mongodb, selecting collection in which want to work
        
    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document inserted in collection:", self.collection.name)
        #self.collection.insert_one(document)
        print("result is:", result)
        return result
        # print("result",result.__inserted_id{ inserted id will give obejct id from mongoDB} 
        
        
    def fetch(self, query=""):
        documents = self.collection.find(query) # query is a where condition , if blank means select * in my sqL, Can pass query for key like query = user_data
        return list(documents)
    
    def delete(self, query=""):
        result = self.collection.delete_one(query)
        print("resilt is",result)
        return result
    
    def update(self,document,query):
        document_to_update = {'$set': document}
        result = self.collection.update_one (query, document_to_update)
        print("result is", result)
        return result