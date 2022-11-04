# You need to import the database connection from mysqlconnection.
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "user_schema"

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #! Create - this is the method we use to creat a new user.
    @classmethod
    def save(cls, data): #! Save returns the id where the data is stored not a list of dictories
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s,%(email)s)"
        return connectToMySQL(DATABASE).query_db(query, data) 
        #! no variable needed due to returing to the database. 

    #! READ ALL
    # Now we use class methods to query our database
    #! Also this is our READ ALL(which showing all users)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting. WHIHC MAKES A LIST OF DICTONIERS
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances (NEW USER) of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users

    #! READ ONE - meaning pull one user to update their info.
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result =  connectToMySQL(DATABASE).query_db(query, data) 
        return User(result[0])

    #! Update - When you update the databases you are POSTing
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id= %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data) 

    #! Delete User
    @classmethod
    def destory(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data) 

