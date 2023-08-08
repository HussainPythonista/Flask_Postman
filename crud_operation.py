from pymongo import MongoClient


'''
Database connectivity using pymongo


File contains mainly 4 operation

-Read Data from database
    - get_all_data()
    - get_one_data(roll_no)
    - The above two function get some deatils from the Database
- Creating Data from database
    - insert_details(roll_no,name,age,class_,section)
    - Add students in the database if the roll no is not present alreay
-Update 
    - update_info(self, roll_no, name, age, class_, section)
    - Updateing existing user with unique id in it

- Delete
    - delete_info(roll_no)
    - Delete the student information from database
'''

class CRUD:
    def __init__(self):
        '''Creating attributes based on our mongodb database information
        '''
        #URL for localhost
        self.url = "mongodb://localhost:27017"
        #Creating access from local host
        self.client = MongoClient(self.url)
        #Access database from local host
        self.db = self.client['Student']
        #Access collection from Database to get documents
        self.collection = self.db['Student_Details']

    def get_all_data(self):
        '''
            Reading data's from the database, to show in html page
        '''
        #creating variable to store all the documents which stored in database
        documents = list(self.collection.find())
        result = []
        for document in documents:
            document['_id'] = str(document['_id'])
            result.append(document)
        return result
    
    def get_one_data(self,roll_no):

        '''Method which helps to access single data from the database, if data present in database which return the information,it will return if data present in database
        it will return "Not Present" if not present in database
        '''

        #Get one data for using build_in find_one method in pymongo
        data=self.collection.find_one({"roll_no":int(roll_no)},{"_id":0})
        if data!=None:
            return data
        else:
            return None
        
        
    def insert_details(self,roll_no,name=None,age=None,class_=None,section=None,class_teacher=None):

        '''
        Getting the parameters like Roll No,Name,Age,Class,Section, and create it into the dictionry boject to store in mongo DB,
        using build_in keyword in pymongo insert_one()
        '''
        data_to_insert={
            "name":name,"age":age,"class":class_,"section":section,"roll_no":roll_no,"class_teacher":class_teacher
        }
        #Inserting data using inset_one method in mongoDB
        self.collection.insert_one(data_to_insert)
        return self.collection
        
    def update_info(self, roll_no, name, age, class_, section,class_teacher):
        '''
        Getting the parameters like Roll No,Name,Age,Class,Section, and create it into the dictionry boject to store in mongo DB,
        using build_in keyword in pymongo 
        update_info(roll_no, name, age, class_, section)

        $set keyword which is useful for updating information 
        '''
        filter_ = {"roll_no": int(roll_no)}
        new_values = {"$set": {
            "name": name,
            "age": age,
            "class": class_,
            "section": section,
            "class_teacher":class_teacher
        }}
        self.collection.update_one(filter_, new_values)

    def delete_info(self,roll_no):
        '''Method which helps to delete single data from the database'''
        filter={"roll_no":int(roll_no)}
        self.collection.delete_one(filter)
        return self.collection
    
    def delete_list_info(self,list_):
        return self.collection.delete_many({"roll_no":{"$in":list_}})
    
cr_test=CRUD()
print(cr_test.get_one_data(175))