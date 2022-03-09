from flask import Flask, render_template, request
from models import connect_db, Cupcake

app.config['SQLALCHEMY_DATABASE_URL']='postgresql://postgres:admin@localhost:5432/cupcake'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.config['SQLALCHEMY_ECHO']=True
app.config['SECRET_KEY']="DELIOUS"


app = Flask(__name__)