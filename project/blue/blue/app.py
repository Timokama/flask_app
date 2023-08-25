import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'hostels.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Text)
    
    students = db.relationship('Student', backref='hostel')

    def __repr__(self):
        return f'<Room "{self.room}...">'

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    course = db.Column(db.String(100))
    hostel_id =db.Column(db.Integer, db.ForeignKey('hostel.id'))

    def __repr__(self):
        return f'{self.name}'


@app.route('/')
def index():
    hostels = Hostel.query.all()
    return render_template('index.html', hostels=hostels)

@app.route('/<int:hostel_id>/', methods=('GET', 'POST'))
def hostel(hostel_id):
    hostel = Hostel.query.get_or_404(hostel_id)
    if request.method == 'POST':
        student = Student(
            firstname=request.form['firstname'],
            lastname=request.form['lastname'],
            email=request.form['email'],
            course=request.form['course']
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('hostel', hostel_id=hostel.id))
    return render_template('hostel.html', hostel=hostel)

@app.route('/students/')
def students():
    students = Student.query.order_by(Student.id.desc()).all()
    return render_template('student.html', students=students)

@app.route('/students/<int:student_id>/')
def student(student_id):
    
    student = Student.query.get_or_404(student_id)
    hostel_id = student.hostel.id
    hostel = Hostel.query.get_or_404(hostel_id)
    
    #hostel = Hostel.query.get_or_404(hostel_id)
    return render_template('student_id.html', student=student, hostel=hostel)

@app.post('/students/<int:student_id>/delete')
def delete(student_id):
    student = Student.query.get_or_404(student_id)
    hostel_id = student.hostel.id
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('hostel', hostel_id=hostel_id))
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        hostel = Hostel(room=request.form['room'])
        db.session.add(hostel)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/students/<int:student_id>/edit/', methods=('GET', 'POST'))
def edit(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        firstname=request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        course = request.form['course']
        #hostel = Hostel(room=request.form['room'], hostel = hostel)

        student.firstname = firstname
        student.lastname = lastname
        student.email = email
        student.course = course
        
        #db.session.add(hostel)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('student',student_id=student.id))

    return render_template('edit.html', student=student)

if __name__=="__main__":
    app.run()