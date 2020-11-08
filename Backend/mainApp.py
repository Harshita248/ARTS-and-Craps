# Author: Sam Shenoi
# Description: This file creates a backend web server for the
#  ARTS-AND-CRAPS project using python flask and MySQL.
#  Instructions for creating the SQL script can be found in
#  the SQLScipt.sql file

from flask import Flask, jsonify
app = Flask(__name__)
import csv
import json
from DAOs.ArtsDAO import ArtsDAO
from DAOs.InstructionDAO import InstructionDAO
from DAOs.MaterialDAO import MaterialDAO
from DAOs.RatingDAO import RatingDAO

aDAO = ArtsDAO()
iDAO = InstructionDAO()
rDAO = RatingDAO()

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/getAllCrafts')
def get_crafts():
    return jsonify(aDAO.selectAll())

@app.route('/getCrafts')
def get_crafts2():
    f = open("out.json")
    j = json.loads(f.read())
    f.close()
    return jsonify(j)

@app.route('/getInstructions/<instruction>')
def get_instructions(instruction):
    return jsonify(iDAO.selectAllInstructions(instruction))

@app.route('/setRating/<name>/<rating>')
def set_rating(name,rating):
    print(name,rating)
    rDAO.insertRating((name,rating))
    return ""



'''
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)
'''



if __name__ == "__main__":
    app.run(port=8080)