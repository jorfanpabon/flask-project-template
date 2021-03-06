from flask import Flask, redirect, render_template, url_for
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)

app.secret_key = getenv('SECRET_KEY')


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return "Hello world"


@app.route('/projects/')
def projects():
    return 'The project page'

    
@app.route('/about')
def about():
    return 'The about page'




