# Author: Sam Shenoi
# Description: This file creates a backend web server for the
#  ARTS-AND-CRAPS project using python flask and MySQL.
#  Instructions for creating the SQL script can be found in
#  the SQLScipt.sql file

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!


