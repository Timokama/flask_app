from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   phone = db.Column(db.String(200)) 
   pin = db.Column(db.Integer, nullable=True)

   
   def __init__(self, name, city, phone, pin):
      self.name = name
      self.city = city
      self.phone = phone
      self.pin = pin

@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
         print('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['city'], request.form['phone'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()
         print('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')
@app.route('/<int:student_id>/')
def student(student_id):
   student= students.query.get_or_404(student_id)
   return render_template('student.html', student=student)

@app.post('/<int:student_id>/delete/')
def delete(student_id):
    name = students.query.get_or_404(student_id)
    db.session.delete(name)
    db.session.commit()
    return redirect(url_for('show_all'))

@app.route('/<int:student_id>/edit', methods=('POST', 'GET'))
def edit(student_id):
   student = students.query.get_or_404(student_id)
   if request.method == 'POST':
      name = request.form['name']
      city = request.form['city']
      phone = request.form['phone']

      student.name = name
      student.city = city
      student.phone = phone
      db.session.add(student)
      db.session.commit()
      return redirect(url_for('show_all'))
   return render_template('edit.html', student = student)
if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)