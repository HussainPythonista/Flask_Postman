#importing Necessary libraries for working on flask application
from flask import Flask, render_template, url_for, request, redirect, flash,jsonify

#Getting CRUD class which create stored in another file 
from crud_operation import CRUD

#Creating flask object from FLask Class
app = Flask(__name__)

#Create access key for passing flash message in HTML page
app.secret_key = "abc123"

#Creating database mongo object CRUD class
db = CRUD()



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
    data=db.get_one_data(roll_no)
    if data == None:
        return jsonify({"message": "Data not found"})

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
        db.delete_info(roll_no)
        return jsonify({"Message":"Student Name : "+ deleted_person["name"]+" get deleted"})
    
    else:
        return jsonify({"Message":"Student information Not Present"})
    

#Run the flask application in 5500 port
if __name__ == "__main__":
    app.run(port=5500)