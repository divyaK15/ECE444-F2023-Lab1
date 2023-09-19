from flask import Flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime as datet

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
@app.route('/')
def index():
    print("Hello World")
    print(datet.utcnow())
    return render_template('index.html', current_time=datet.utcnow())


@app.route('/user/<name>')
def user(name):
    print(datet.utcnow())
    return render_template('user.html', name=name, current_time=datet.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
