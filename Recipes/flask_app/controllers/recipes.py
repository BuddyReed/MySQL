from flask_app import app, render_template, redirect, request, bcrypt, session, flash
from flask_app.models.user import User


    
    #! This will usually go into a different controller. This is a page after register or login
@app.route ('/recipes')
def things():
    return render_template('recipes.html')

# CREATE New Recipe

@app.route('/recipes/new')
def new_recipe():
    return render_template('new_recipes.html')



