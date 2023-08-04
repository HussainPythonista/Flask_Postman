#importing Necessary libraries for working on flask application
from flask import Flask, render_template, url_for, request, redirect, flash,jsonify

#Getting CRUD class which create stored in another file 
from crud_operation import CRUD

from flask_cors import CORS

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}}) # Enable CORS for all origins
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
#Creating flask object from FLask Class
app = Flask(__name__)

#Create access key for passing flash message in HTML page
app.secret_key = "abc123"

#Creating database mongo object CRUD class
db = CRUD()


from flask import Flask, jsonify
from crud_operation import CRUD
from flask_cors import CORS



@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4200'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    return response


@app.route("/")
def stu_info():

    '''Reading all the information which stores in Database, and show it in HTML Page, 
    calling get_all_data() method from CRUD class, and access all the information which stored in mongodb'''
    datas = db.get_all_data()
    #Rendering to the main page which will help us to get all the information
    #return render_template("student_info.html", datas=datas)
    #return datas
    datas = db.get_all_data()
    return jsonify(datas)


@app.route("/get_one/<roll_no>",methods=["GET"])
def get_one_student_info(roll_no):
    data=db.get_one_data(roll_no=roll_no)
    if data == None:
        
        return jsonify({"message": "Data Not Present"})
    else:
    #data['_id'] = str(data['_id'])
        return jsonify(data)

#Deleting the existing record
@app.route("/delete/<roll_no>",methods=['DELETE'])
def delete_stu(roll_no):
    '''
    Getting roll_no from htmlpage and push it to the CRUD class to delete the record from mongodb
    '''

    #filter_data={"roll_no":roll_no}
    deleted_person=db.get_one_data(roll_no)
    if deleted_person!=None:
        db.delete_info(str(roll_no))
        return jsonify({"Message":"Deleted"})#"Student Name : "+ deleted_person["name"]+" get deleted"})
    
    else:
        return jsonify({"Message":"Student information Not Present"})
    
@app.route("/add", methods=["POST","PUT"])
def add_edit_students():
    '''
    Combined function for adding and editing student information in the database.
    If the roll number already exists, it updates the information. If the roll number does not exist,
    it adds the data to the MongoDB.

    The request data should be sent in JSON format with the following structure:
    {
        "roll_no": "<roll_no>",
        "name": "<name>",
        "age": "<age>",
        "class": "<class>",
        "section": "<section>"
    }

    If the roll number already exists, it updates the information in the database.
    If the roll number is not present, it inserts the data into the database.

    Returns a JSON response with the appropriate message.
    '''

    data = request.get_json()
    roll_no = data["roll_no"]

    # Checking for existence
    checking = db.get_one_data(roll_no)
    
    if checking is None:
        name = data.get("name")
        class_ = data.get("class")
        section = data.get("section")
        age = data.get("age")
        class_teacher = data.get("class_teacher")
        
        db.insert_details(roll_no=roll_no, name=name, age=age, class_=class_, section=section, class_teacher=class_teacher)
        return jsonify("Yah!!! Student information created")
    else:
        existing_data = db.get_one_data(roll_no)

        name = data.get("name", existing_data["name"])
        class_ = data.get("class", existing_data["class"])
        section = data.get("sec", existing_data["sec"])
        age = data.get("age", existing_data["age"])
        class_teacher = data.get("class_teacher", existing_data["class_teacher"])

        db.update_info(roll_no=roll_no, name=name, age=age, class_=class_, section=section, class_teacher=class_teacher)
        return jsonify("The Data already exists!!! So I updated the Student information")
    
    
@app.route("/add_many",methods=["POST"])
def add_many():
    # Process the data, such as inserting into a database or performing any other desired operations
    data = request.get_json()
    db.collection.insert_many(data)

    return {"MESSAGE":"Data Inserted"}

if __name__ == "__main__":
    app.run()
    
@app.route("/test")
def test_route():
    return "This is a test shit"
#Run the flask application in 5500 port
if __name__ == "__main__":
    app.run(port=5500)