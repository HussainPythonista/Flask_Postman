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
    return jsonify(datas)#render_template("student_info.html", datas=datas)


@app.route("/add", methods=["GET", "POST"])
def addStudents():
    '''Using addStudents() function we can acess all the details which which enters in HTML page, 
    add store it in the database, if the roll no is not present already,

    If our request is post first check the roll no is already exist we reply some error on that, 
    and we check the roll no 4 value length, if satisfies those condition we store the data's into the Database
    '''
    # If request is Post we check it and stores in database


    if request.method == "POST":

        #Check if roll_no already exist and 4 value long, if it satisfies we store data or we throws some error
        roll_no = request.form["roll No"]
        if not roll_no.isdigit() or len(roll_no) != 4:
            return jsonify({"message":"Roll number must contain 4 digits"})
            #return redirect(url_for("addStudents"))

        existing_user = db.get_one_data(roll_no)
        if existing_user != "Not Present":
            #flash("Roll number already exists", category="error")
            return jsonify({"message":"Roll number already exists"})
            #return redirect(url_for("addStudents"))

        #Getting age, class,section and name from html document
        age = request.form["age"]
        class_ = request.form["class"]
        section = request.form["section"]
        name = request.form["name"]

        #Stores in database using buildin method in pymongo
        db.insert_details(name=name, age=age, class_=class_, roll_no=roll_no, section=section)

        return jsonify({"message": "Student created"})

        #Flashing message to the user
        #flash("Student created", category="success")
        #Redirect to main page
        #return redirect(url_for("stu_info"))

    return render_template("add_students.html")





@app.route("/edit/<roll_no>", methods=["GET", "POST","PUT"])
def edit_info(roll_no):
    '''
    Using edit_info(roll_no) function, if it is Post request, if he change the roll no we check it is already exist or no
    other information is we update as like without checking

    
    '''

    #Check if it is Post request we check roll_no already exist and 4 value long, 
    # if it satisfies we store data or we throws some error
    if request.method == "POST":
        roll_no = request.form["roll No"]

        # #Checking condition if it satisfies we load data's into mongo db
        # if not roll_no.isdigit() or len(roll_no) != 4:
        #     #flash("Roll number must contain 4 digits", category="error")
        #     return jsonify({"message":"Roll number must contain 4 digits"})#redirect(url_for("edit_info", roll_no=roll_no))
        # existing_user = db.get_one_data(roll_no)
        # if existing_user != "Not Present":
        #     #flash("Roll number already exists", category="error")
        #     #return redirect(url_for("edit_info",roll_no=roll_no))
        #     return  jsonify({"message":"Roll number already exists"})
        #Getting and storing information in variables
        age = request.form["age"]
        class_ = request.form["class"]
        section = request.form["section"]
        name = request.form["name"]

        #Updating information in database using pymongo buildin method
        db.update_info(roll_no=roll_no, name=name, age=age, class_=class_, section=section)
        flash("Student Information Updated", category="success")
        response={"message":"student updated"}
        return response#redirect(url_for("stu_info"))

    info_existing_user = db.get_one_data(roll_no)
    return  {"message":"Information gathered"}#render_template("edit_students.html", info=info_existing_user)




#Deleting the existing record
@app.route("/delete/<roll_no>",methods=['DELETE'])
def delete_stu(roll_no):
    '''
    Getting roll_no from htmlpage and push it to the CRUD class to delete the record from mongodb
    '''
    db.delete_info(roll_no)

    #Showing information the student information get deleted
    flash("Student Information Deleted")
    response= {"message":"deleted"}
    #Redirect to the home page
    #return redirect(url_for("stu_info"))
    return response

#Run the flask application in 5500 port
if __name__ == "__main__":
    app.run(port=5500)