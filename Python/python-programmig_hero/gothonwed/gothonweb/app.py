from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', 'Nobody')
    greet = request.args.get('greet', 'Hello')

    if name:
        greetings = f"{greet}, {name}"
    else:
        greetings = f'{greet}'

    return render_template('index.html', greetings=greetings)