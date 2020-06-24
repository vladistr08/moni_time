from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/moni_time"
mongo = PyMongo(app)

@app.route('/login', methods=['POST'])
def post_loin():
    req_data = request.get_json()
    req_data = dict(req_data)

    user = req_data["username"]
    password = req_data["password"]
    
    x = mongo.db.users.find_one({"username":user,"password":password})
    return "ok" if x != None else "404"

@app.route('/register', methods=['POST'])
def post_register():
    req_data = request.get_json()
    req_data = dict(req_data)

    email = req_data["email"]
    username = req_data["username"]
    password = req_data["password"]

    for x in mongo.db.users.find():
        if x["email"] == email or x["username"] == username:
            return "User deja existent!!!"

    x = {"username":username, "email":email, "password":password}
    mongo.db.users.insert_one(x)
    return "User-ul a fost adaugat cu succes"

@app.route('/list/<username>')
def getProcesses(username):
    user_profile = mongo.db.users.find_one({'username':username})
    return str(user_profile)

app.run(host = '0.0.0.0', debug=False)