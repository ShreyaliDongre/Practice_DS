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


if __name__=='__main__':
    app.run(debug=True)



