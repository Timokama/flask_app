import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'all.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class first_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    #score_id = db.relationship('second_table', backref = 'first_table')

    def __repr__(self):
        return f'Your name is: {self.name}'

    
class second_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=True)

    name_id = db.Column(db.Integer, db.ForeignKey('first_table.id'), nullable=True)

    def __repr__(self):
        return f' {self.score}'

# def sum(self, score,total=0):
#     total += score
#     return f'{total}'
# total = sum(second_table, 12)
# print(total)

@app.route('/')
def index():
    names = first_table.query.all()
    score = second_table.query.filter(db.and_(second_table.name_id == first_table.id)).all()
    return render_template('index.html', names=names, score = score)

@app.route('/<int:name_id>/')
def name(name_id):
    f_name=first_table.query.get_or_404(name_id)
    score = second_table.query.get_or_404(name_id)
    return render_template('name.html', name=f_name,score_id=score)

@app.route('/create',methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name1= first_table(name=request.form['name'])
        score= second_table(score=request.form['score'])
        db.session.add_all([name1,score])
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:name_id>/edit', methods=('POST', 'GET'))
def edit(name_id):
    names = first_table.query.get_or_404(name_id)
    scores = second_table.query.get(name_id)
    if request.method == 'POST':
        name=request.form['name']
        score=request.form['score']
        names.name = name
        scores.score = score
        db.session.add_all([names, scores])
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html',name=names,score=scores)

@app.post('/<int:name_id>/delete/')
def delete(name_id):
    name = first_table.query.get_or_404(name_id)
    score = second_table.query.get_or_404(name_id)
    db.session.delete(name)
    db.session.delete(score)
    db.session.commit()
    return redirect(url_for('index'))
