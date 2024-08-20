from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MDBH:
    def __init__(self, collection="user"):
        
         
        uri = "mongodb+srv://65himanshusingla:hsingla@cluster0.icffm7p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
            
        self.db = client['traderjournal']
        
        self.collection = self.db[collection]
        
        
        
    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document inserted successfully in:", self.collection.name)
        print("result is:", result)
        return result
        
    
    def fetch(self, query=""):
        result = self.collection.find(query)
        print("result is:", result)
        return list(result)
    
    def delete(self, query=""):
        document = self.collection.delete_one(query)
        print("Document deleted successfully..", document)
        return document
    
    def update(self,document,query=""):
        document_to_update = {"$set": document}
        result = self.collection.update_one(query, document_to_update)
        print("result is:", result)
        return result