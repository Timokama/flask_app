from flask import Flask, render_template, request, url_for, redirect
import os
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER 

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        image = request.form[os.path.join(app.config['UPLOAD_FOLDER'], image)]
        return redirect(url_for('result', image=image))
    return render_template('home.html')


@app.route("/result", methods=['GET', 'POST'])
def result():
    
    image = request.form.get('image')
    return render_template("result.html", image=image)


if __name__ == "__main__":
    app.run()
