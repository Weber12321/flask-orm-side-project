import configparser
from datetime import datetime

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from utils.logger_helper import get_logger

_logger = get_logger('server')

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['DEV_FLASK_CONFIG']['sqlalchemy_database_uri']



db = SQLAlchemy(app)

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.String(9), primary_key=True)
    items = db.Column(db.String(30))
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.String(100), unique=True, nullable=False)
    card = db.Column(db.String(30), nullable=True)
    status = db.Column(db.String(10), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)

@app.route('/')
def entry_page():  # put application's code here
    return redirect(url_for('index_page'))

@app.route('/index')
def index_page():  # put application's code here
    return "HI"

@app.route('/account_list')
def show_list():
    pass

@app.route('/input/{id}', methods=['GET', 'POST'])
def input_data():
    pass

@app.route('/update/{id}', methods=['PUT', 'POST'])






if __name__ == '__main__':
    app.run(host=config['DEV_FLASK_CONFIG']['host'], port=config['DEV_FLASK_CONFIG']['port'])
