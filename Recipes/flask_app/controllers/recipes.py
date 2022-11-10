from flask_app import app, render_template, redirect, request, bcrypt, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


# CREATE New Recipe

@app.route('/recipes/new')
def new_recipe():
    if "user_id" not in session:
        return redirect('/logout')
    return render_template('new_recipes.html')

@app.route("/recipes/create", methods=['POST'])
def create_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    #! This calls on the save model in order to save to the database
    Recipe.save(request.form)
    return redirect('/recipes')


#! This will usually go into a different controller. This is a page after register or login
@app.route ('/recipes')
def things():
    if "user_id" not in session:
        return redirect('/logout')
    return render_template('recipes.html', recipes = Recipe.get_all())

@app.route('/recipes/<int:id>')
def show_recipe(id):
    data = {'id' : id}
    return render_template('show_recipe.html', recipe = Recipe.get_one(data) )

#! Update
@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    data = {'id' : id}
    return render_template('edit_recipe.html', recipe = Recipe.get_one(data))

@app.route('/recipes/update', methods=['POST'])
def update_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/edit/{request.form['id']} ")
    Recipe.update(request.form)
    return redirect('/recipes')

#! Delete
@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    data = {"id" : id}
    Recipe.destory(data)
    return redirect('/recipes')
