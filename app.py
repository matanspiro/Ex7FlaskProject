from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return "This is the homepage"

@app.route('/catalog')
def catalog():
    return "This is the catalog page"

@app.route('/about')
def getAboutFunc():
    return redirect(url_for('about'))

@app.route('/about')
def about():
    return redirect('/catalog')

if __name__ == '__main__':
    app.run(debug=True)
