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


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getCrafts')
def get_crafts2():
    f = open("out.json")
    j = json.loads(f.read())
    f.close()
    return jsonify(j)



if __name__ == "__main__":
    app.run(port=8080)