from flask import Flask, render_template, redirect, request

app = Flask(__name__)
@app.route('/greet', methods=['POST', 'GET'])
@app.route('/', methods=('POST', 'GET'))
def index():
    hello = "Hello World!"
    if request.method == 'POST':
        hello = request.form['hello']

        name = request.form['name']

        greet = f'{hello}, {name}'
        return render_template('index.html', greet = greet, name=name, hello = hello)
    return render_template('form.html')

if __name__ == '__main__':
    app.run()