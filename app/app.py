from flask import Flask ,request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

MONGOOB_URI = os.environ.get(
    "MONGOOB_URI",
    "mongodb://localhost:27017/"
)

client = MongoClient(MONGOOB_URI)

#database and collection
db = client.flask_db
colection =db.data


#home route
@app.route("/")
def index():
    return f"Welcome to to aryan app! the current tiem is : {datetime.now()}"




# get and post data

app.route("/data",method=["GET","POST"])
def data():
    if request.method == "POST":
        data  = request.get_json()

        if not data :
            return jsonify({"error":"JSON data is required"}),400

        collection.insert_one(data) 
        return jsonify({"status":"data inserted"}),201

    elif request.method =="GET":
        data = list (colection.find({},{"_id":0}))
        return jsonify(data),200


# RUN APPLICATION

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000 ,debug=True)