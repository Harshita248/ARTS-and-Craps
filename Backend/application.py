# Author: Sam Shenoi
# Description: This file creates a backend web server for the
#  ARTS-AND-CRAPS project using python flask and MySQL.
#  Instructions for creating the SQL script can be found in
#  the SQLScipt.sql file

from flask import Flask, jsonify
app = Flask(__name__)
from flask_swagger_ui import get_swaggerui_blueprint
import csv
from flask_swagger import swagger

from DAOs.ArtsDAO import ArtsDAO

aDAO = ArtsDAO()

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/getAllCrafts')
def get_crafts():

    return jsonify(aDAO.selectAll())


## TODO: Implement Swagger documentation
@app.route("/spec")
def spec():
    return jsonify(swagger(app))



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
    data = []
    with open('Arts.tsv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter='\t')
      print("Use `ArtsAndCraps`;")
      for row in spamreader:
          for r in range(0,len(row)):
              row[r] = row[r].replace('  ',' ')
              row[r] = row[r].replace('\'','\\\'')
              row[r] = row[r].replace('\"','\\\"')
          print("INSERT INTO Arts (Name, Img) VALUES (\"%s\",\"%s\");" % (row[0],0))
          materials = row[1].split("\n")
          for m in materials:
              if m != "" and m!=" ":
                print("INSERT INTO Material(Name,Material) VALUES (\"%s\",\"%s\");" % (row[0],m))
          steps = row[2].split("\n")
          stepcounter = 1
          for s in range(0,len(steps)):
            step = steps[s]
            if step != "" and step != " "
                print("INSERT INTO Instruction(Name,Instruction,StepNumber) VALUES (\"%s\",\"%s\",\"%s\");" % (row[0],step,s))
                stepcounter = stepcounter + 1




    #app.run()