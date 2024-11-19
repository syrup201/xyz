from flask import Flask # type: ignore
app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the home page'

@app.route('/hello')
def hello():
    return 'Hello'