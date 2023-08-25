from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/hello')
def index():
    return render_template('index.html')

@app.route('/input', methods=('POST', 'GET'))
def input():
    if request.method == 'POST':
        greet = request.form['greet']
        name = request.form['name']
        greeting = f'{greet}, {name}'
        return render_template('input.html', greeting = greeting)
    return render_template('form.html')

if __name__ == "__main__":
    app.run()