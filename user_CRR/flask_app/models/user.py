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
    # @classmethod
    # def save(cls, data):

    # Now we use class methods to query our database
    #! Also this is our READ ALL(which showing all users)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users