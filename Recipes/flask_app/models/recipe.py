from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = 'recipes'

class Recipe:

    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instuctions = data['instuctions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.user_id = data['user_id'] #! Ask Tyler About this
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instuctions, date_made, under_30, user_id) VALUES (%(first_name)s, %(description)s, %(instuctions)s, %(date_made)s, %(under_30)s, %(user_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

