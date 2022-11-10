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
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.user_id = data['user_id'] #! This is a many to many relationship. So you want to access the user id in order to put the many recipes.
        self.first_name = data['first_name'] # Adding this allows you to show the who the recipe was posted by. Also referenec the query in get all.
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #! Create
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s)"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result


    #! This method shows all the user recipes on the Recipes page.. 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        # make sure to call the connectToMySQL function with the schema you are targeting. WHICH MAKES A LIST OF DICTONIERS
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances (NEW RECIPES) of recipes
        recipes = []
        # Iterate over the db results and create instances of recipes with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes
    
    # Read one and adding the one to many relationship 
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;" #! STUDYYYY
        result =  connectToMySQL(DATABASE).query_db(query, data) 
        return cls(result[0])
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True 
        if len(recipe['description']) < 3:
            flash('Description must be at least 3 chararacters')
            is_valid = False
        return is_valid
    
    #!UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under_30=%(under_30)s, user_id=%(user_id)s WHERE id= %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data) 

    @classmethod
    def destory(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)