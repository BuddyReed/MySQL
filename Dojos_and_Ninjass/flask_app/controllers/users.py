from flask_app import app, render_template, request, redirect
#This is importing your cless(models) User into the file to access
from flask_app.models.user import Dojo

#Read All route pulling all Dojo locations.
@app.route('/')
def show_dojos():
    return render_template('user_new.html', dojos = Dojo.get_all())

#Route to create new dojo. This route is placed on the root page
@app.route("/create", methods=['POST'])
def new_user():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/')

#This route is fot the New Ninjas page. It is used to render page and create new Ninjas to a Dojo
@app.route('/ninjas')
def index():
    return render_template('index.html', dojos = Dojo.get_all())



@app.route('/dojos')
def dojos():
    return render_template('show_user.html')




# #! CREATE - When POSTing to your database you need two routes
# @app.route('/users/new')
# def user_new():
#     return render_template("user_new.html")

# @app.route("/users/create", methods=['POST'])
# def new_user():
#     print(request.form)
#     User.save(request.form)
#     return redirect('/')

# #! READ ALL (ROUTE) - pulling all user from database
# @app.route('/')
# def index():
#     return render_template('index.html', users = User.get_all())

# #! READ ONE Showing the users info by itseld. this isn't tied to the class

# @app.route('/user/show/<int:id>')
# def show_user(id):
#     data = {"id" : id}
#     return render_template('show_user.html', user = User.get_one(data))


# #! UPDATE - Your need two routes to update. One for the main page the other to process the update.
# @app.route('/user/edit/<int:id>')
# def edit_user(id):
#     print(id)
#     data = {"id" : id}
#     return render_template('edit_user.html', user = User.get_one(data))

# #! When you hendle data being input by user it is a POST route.
# @app.route('/user/update', methods=['post'])
# def update_user():
#     print(request.form)
#     User.update(request.form)
#     return redirect('/')

# #! DELETE

# @app.route('/user/delete/<int:id>')
# def delete_user(id):
#     data = {"id" : id}
#     User.destory(data)
#     return redirect('/')