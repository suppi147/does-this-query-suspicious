from flask import Flask, render_template

app = Flask(__name__)

messages = [{'query':'SELECT 1'}]

@app.route('/')
def index():
    return render_template('check/index.html', messages=messages)
