from flask import Flask

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return "<h1>Page not found.</h1>"


@app.route('/')
def index():
    return "Hello world Flask"