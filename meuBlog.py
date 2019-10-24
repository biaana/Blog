from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from form import RegistratioForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Site.db'
app.config['SECRET_KEY'] ='dtg098g70f86hhfg70f45dsfsf6dg56r'
db = SQLAlchemy(app)

Class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), u, nullable=False)

def__repr__(self):
    return '<User %r>' %self.username

@app.route('/')
def index():
    return()
