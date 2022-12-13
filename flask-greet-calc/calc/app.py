from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add(a, b):
    sum = a+b
    return f"<body>{sum}</body>"

@app.route('/sub')
def subtract(a, b):
    subt = a - b
    return f"<body>{subt}</body>"

@app.route('/mult')
def multiply(a, b):
    multi = a * b
    return f"<body>{multi}</body>"

@app.route('/div')
def divide(a, b):
    divi = a / b
    return f"<body>{divi}</body>"

app.run(host='0.0.0.0', port=81)
