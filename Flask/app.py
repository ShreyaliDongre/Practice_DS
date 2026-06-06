from flask import Flask
#WSGI stands for Web Server Gateway Interface, it is a specification for a universal interface between the web server and web applications.
# The WSGI specification defines how a web server communicates with web applications, and how web applications can be chained together to process one request.
app = Flask(__name__)
 #this is the main file of the flask app, it will run the app and import the routes
#this creates an instance of the Flask class, which is the main class of the Flask framework. 
# The __name__ variable is a special variable that is set to the name of the module in which it is used. 
# In this case, it will be set to 'app', which is the name of this file.

@app.route('/')
# this is a decorator that tells Flask what URL should trigger the function that follows it.
def hello_world():
    return 'Hello, I am shreyali dongre!'

@app.route('/about')
def about():
    return 'This is a simple Flask application created by Shreyali Dongre.'



if __name__ == '__main__':
    app.run(debug=True) 
# the debug=True argument enables the debug mode, which provides a debugger and reloader for the application.
# this checks if the script is being run directly (as the main program) and if so, it calls the run() method of the Flask app to start the development server.  
