from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Site.db'
db = SQLAlchemy(app)

Class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(20), u, nullable=False)

def__repr__(self):
    return '<User %r>' %self.login 

if (__name__) == ("__main__"):
    app.run(debug=True)
