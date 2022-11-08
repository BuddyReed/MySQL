from flask_app import app, render_template, request, redirect
#This is importing your cless(models) User into the file to access
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#! Go to server to add Ninja 

#This route is fot the New Ninjas page. It is used to render page and create new Ninjas to a Dojo
@app.route('/ninjas')
def index():
    return render_template('index.html', dojos = Dojo.get_all())

@app.route("/ninjas/create", methods=['POST'])
def new_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect(f"/dojos/show/{request.form['dojo_id']}") #! STUDY STUDY - 

