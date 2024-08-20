from flask import *
from flask_restful import Api, Resource

awebapp = Flask("trader")
api = Api(awebapp)

class helloworld(Resource):
    
    def get(self, name, test):
        return {"name": name, "test": test}


api.add_resource(helloworld, "/helloworld/<string:name>/<string:test>")





if __name__ == "__main__":
    
    awebapp.run()
        