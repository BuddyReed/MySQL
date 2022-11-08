# You need to import the database connection from mysqlconnection.
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja #! This need to be import because we are making a ninja on this page by calling all the ninjas in the location

DATABASE = "dojo_and_ninjas_schema"

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        # self.last_name = data['last_name']
        # self.email = data['email']
        # self.created_at = data['created_at']
        # self.updated_at = data['updated_at'] #! WHY NOT WORKING

    #! Create - this is the method we use to creat a new dojo.
    @classmethod
    def save(cls, data): #! Save returns the id where the data is stored not a list of dictories
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL(DATABASE).query_db(query, data) 
        #! no variable needed due to returing to the database. 

    #! READ ALL
    # Now we use class methods to query our database
    #! Also this is our READ ALL(which showing all dojos)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting. WHIHC MAKES A LIST OF DICTONIERS
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances (NEW dojo) of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    #! READ ONE - meaning pull one dojo to update their info.
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result =  connectToMySQL(DATABASE).query_db(query, data) 
        return Dojo(result[0])

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results =  connectToMySQL(DATABASE).query_db(query, data) 
        print(results)
        dojo = Dojo(results[0])
        print(dojo.name)
        for result in results:
            temp_ninja = {
                'id' : result['ninjas.id'],
                'first_name' : result['first_name'],
                'last_name' : result['last_name'],
                'age' : result['age'],
                'dojo_id' : result['dojo_id'],
                'created_at' : result['created_at'],
                'updated_at' : result['updated_at'],
            }
            dojo.ninjas.append(Ninja(temp_ninja))
        return dojo
    
    #! Update - When you update the databases you are POSTing
    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id= %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data) 

    #! Delete dojo
    @classmethod
    def destory(cls, data):
        query = 'DELETE FROM dojos WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data) 

