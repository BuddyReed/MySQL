from flask_app import app, render_template
#This is importing your cless(models) User into the file to access
from flask_app.models.user import User


#! READ ALL
@app.route('/')
def index():
    return render_template('index.html', users = User.get_all())

#! Update
@app.route('/users/new')
def user_new():
    return render_template("user_new.html")