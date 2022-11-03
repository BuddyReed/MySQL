from flask import Flask, render_template, redirect, session, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance(object) of the Flask class called "app" basically assingmnet Flask class to app
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello Buddy!'  # Return the string 'Hello World!' as a response

from user import User 

@app.route('/users') #This forward / is the route of the web page
def users():
    return render_template("read.html", users = User.get_all()) 

@app.route('/users/new')
def users_new():
    print("It Works")
    print(request.form)
    return render_template('create.html')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)   
