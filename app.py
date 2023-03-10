from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017")


# @app.route("/")
# def hello():
#     database = client.hari
#     collection = database.crud
#     collection.insert_one({
#         "id": 1,
#         "name": "Hari",
#         "language": "tamil"
#     })
#     print("Success")
#     client.close()
#     return "Helloworld"


if __name__ == "__main__":
    app.run(debug=True)
