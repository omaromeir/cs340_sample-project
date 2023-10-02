from flask import Flask, request, jsonify #flask is a minimal framework in Python
from flask_cors import CORS, cross_origin
from db import MyDB
import psycopg2 #postgreSQL driver for python

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.debug = True

# Local host db postgres properties
host_url = "localhost"
host_port = "5432"

@app.route("/")
@cross_origin()
def main():
    return "<p>This is the main page.</p>"

@app.route("/dat", methods = ['POST'])
@cross_origin()
def get_data():
	query = request.get_data()
	db = MyDB()
	results = db.get_data(query)
	return jsonify({
        'status': 'success',
        'results': results
    })
 
