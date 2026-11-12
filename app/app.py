from flask import Flask ,request, jsonify
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

# MONGOOB_URI = os.environ.get(
#     "MONGOOB_URI",
#     "mongodb://localhost:27017/"
# )


MONGODB_URI = os.environ.get("MONGODB_URI")


client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=5000
    
    )

#database and collection
db = client.flask_db
collection =db.data


# test DATABASER MONGOdb
try:
    client.admin.command("ping")
    print("MOongoDb is connected successfully!")
except Exception as e :
    print("mongoDB connection failed")





#home route
@app.route("/")
def index():
    return f"Welcome to to aryan app! the current tiem is : {datetime.now()}"




# get and post data

@app.route("/data", methods=["GET", "POST"])
def data():

    if request.method == "POST":

        data = request.get_json()

        if not data:
            return jsonify({"error": "JSON data is required"}), 400

        collection.insert_one(data)

        return jsonify({"status": "Data inserted"}), 201

    elif request.method == "GET":

        records = list(collection.find({}, {"_id": 0}))

        return jsonify(records), 200

# RUN APPLICATION

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000 ,debug=True)
