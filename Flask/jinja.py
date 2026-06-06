# This code defines a simple Flask web application with multiple routes. 
# It uses Jinja templates to render HTML pages and handles both GET and POST requests. 
#jinja is a templating engine for Python, it is used to create HTML templates that can be rendered with dynamic data.
'''
jinja 2 uses {% %} for statements, {{ }} for expressions to print to the template output, and {# #} for comments.

'''

from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about',methods=['GET'])
def about():
    return "<html><body><h1>About Me</h1><p>This is a simple Flask application created by Shreyali Dongre.</p></body></html>"

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"<html><body><h1>Hello, {name}!</h1><p>Thank you for submitting the form.</p></body></html>"
    else: 
        return render_template('submit.html')

#variable Rules:
@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='You have passed!'
    else:
        res='You have failed!'
    return render_template('result.html',result=res)

if __name__=='__main__':
    app.run(debug=True)



