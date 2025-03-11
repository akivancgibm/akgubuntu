from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return 'Hello World!'

class Thank (Resource):
    def get(self):
        return 'TY!'
    
class Bau (Resource):
     def get(self):
	      return 'BAU2025!'	

api.add_resource(Greeting, '/') # Route_1
api.add_resource(Thank, '/ty') # Route_2
api.add_resource(Bau, '/bau') # Route_3

if __name__ == '__main__':
    app.run('0.0.0.0','3333')
