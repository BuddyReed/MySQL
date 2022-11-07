# You need to import the database connection from mysqlconnection.
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "dojo_and_ninjas_schema"

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] #! WHY NOT WORKING

    #! Create - this is the method we use to creat a new ninja.
    @classmethod
    def save(cls, data): #! Save returns the id where the data is stored not a list of dictories
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data) 
        #! no variable needed due to returing to the database. 

    #! READ ALL
    # Now we use class methods to query our database
    #! Also this is our READ ALL(which showing all ninjas)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting. WHIHC MAKES A LIST OF DICTONIERS
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances (NEW ninja) of ninjas
        ninjas = []
        # Iterate over the db results and create instances of ninjas with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    #! READ ONE - meaning pull one ninja to update their info.
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        return ninja(result[0])

    # #! READ ONE - Showing all ninjas that belong to a certain 
    # @classmethod
    # def get_one_with_ninjas(cls, data):
    #     query = 'SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.id = dojos.id WHERE ninjas.id = %(id)s;'
    #     results =  connectToMySQL(DATABASE).query_db(query, data) 
    #     print(results)

        
    #! Update - When you update the databases you are POSTing
    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id= %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data) 

    #! Delete ninja
    @classmethod
    def destory(cls, data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data) 

