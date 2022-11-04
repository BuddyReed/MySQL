from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance(object) of the Flask class called "app" basically assingmnet Flask class to app
app.secret_key = 'key my name'
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello Buddy!'  # Return the string 'Hello World!' as a response

@app.route('/') #This forward / is the route of the web page
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    print("Got Info")
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    session['username'] = request.form['name']
    session['campus'] = request.form['location']
    session['lang'] = request.form['language']
    session['commenttxt'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def submit_form():
    return render_template('result.html')

# @app.route('/process')
# def submit_form():
#     print('Form Submitted')
#     print(request.form)
#     return('/result')


# @app.route('/play') #Creating a variable within you route
# def play():
#     return render_template("play.html")

# @app.route('/play/<int:num>') #Creating a variable within you route
# def plays(num):
#     return render_template("play_num.html", num = num)

# @app.route('/play/<int:num>/<string:color>') #Creating a variable within you route
# def play_color(num,color):
#     return render_template("play_color.html", num = num, color = color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



