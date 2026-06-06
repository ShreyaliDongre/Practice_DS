from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "<html><body><h1>About Me</h1><p>This is a simple Flask application created by Shreyali Dongre.</p></body></html>"


if __name__=='__main__':
    app.run(debug=True)



