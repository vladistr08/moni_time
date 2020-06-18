from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/moni_time"
mongo = PyMongo(app)

@app.route('/upload', methods=['POST'])
def post_json():
    req_data = request.get_json()
    mongo.db.Prox.insert(dict(req_data))
    return dict(req_data)

app.run(host = '0.0.0.0')