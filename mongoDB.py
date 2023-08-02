# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/data', methods=['GET'])
# def get_data():
#     data = {'name': 'John Doe', 'age': 30}
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(host=5500)

from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Access a specific database
db = client['Student']

collection=db["Student_Details"]

# data={"Name":"Mohamed","Age":26,"Class":"XII","Sec":"A"}

# collection.insert_one(data)

# def insert_document(data):
#     print(data)

# student_data=[
#     {"name": "Alice", "age": 12, "class": 6, "sec": "A", "roll_no": "10001"},
#     {"name": "Bob", "age": 13, "class": 7, "sec": "B", "roll_no": "10002"},
#     {"name": "Charlie", "age": 11, "class": 5, "sec": "C", "roll_no": "10003"},
#     {"name": "David", "age": 14, "class": 8, "sec": "D", "roll_no": "10004"},
#     {"name": "Eve", "age": 12, "class": 6, "sec": "E", "roll_no": "10005"},
#     {"name": "Frank", "age": 13, "class": 7, "sec": "F", "roll_no": "10006"},
#     {"name": "Grace", "age": 11, "class": 5, "sec": "G", "roll_no": "10007"},
#     {"name": "Harry", "age": 14, "class": 8, "sec": "H", "roll_no": "10008"},
#     {"name": "Ivy", "age": 12, "class": 6, "sec": "I", "roll_no": "10009"},
#     {"name": "Jack", "age": 13, "class": 7, "sec": "J", "roll_no": "10010"}
# ]

# collection.insert_many(student_data)

#Get Documents in collection

# Retrieve all documents

# collection.insert_one({"name": "Mohamed", "age": 23, "class": 12, "sec": "A", "roll_no": "10011"})
# print("Insert success")
# filter_ = {"roll_no": 10002}  # Fix the variable name to filter_

# new_values = {"name": "KUPPU", "age": "age", "class": "class_", "sec": "section"}

# result = collection.update_one(filter_, {"$set": new_values})
# print(list(collection.find()))
