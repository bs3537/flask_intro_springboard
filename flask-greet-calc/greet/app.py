from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def index():
    return 'Welcome'

@app.route('/welcome/home')
def home():
    return 'Welcome home'

@app.route('/welcome/back')
def back():
    return 'Welcome back'

app.run(host='0.0.0.0', port=81)