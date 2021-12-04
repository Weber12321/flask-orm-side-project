import ast

from datetime import datetime

import flask_login
from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

from utils.create_table import create_table_if_not_exist
from utils.helper.config_helper import get_config
from utils.helper.logger_helper import get_logger

_logger = get_logger('server')

config = get_config()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['DEV_FLASK_CONFIG']['sqlalchemy_database_uri']
app.config['SECRET_KEY'] = config['DEV_FLASK_CONFIG']['secret_key']

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

db = SQLAlchemy(app)

class User(flask_login.UserMixin):
    pass

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String(30))
    date_info = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.String(100), nullable=False)
    card = db.Column(db.String(30), nullable=True)
    status = db.Column(db.String(30), nullable=False)
    purpose = db.Column(db.String(100))
    insert_time = db.Column(db.DateTime, default=datetime.now)
    insert_by = db.Column(db.String(30), default='Weber')
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)
    update_by = db.Column(db.String(30), default='Weber')
    description = db.Column(db.String(300), nullable=True)

    def __init__(self, items, date_info, amount, payment, card,
                 status, purpose, insert_time, insert_by,
                 update_time, update_by, description):

        self.items = items
        self.date_info = date_info
        self.amount = amount
        self.payment = payment
        self.card = card
        self.status = status
        self.purpose = purpose
        self.insert_time = insert_time
        self.insert_by = insert_by
        self.update_time = update_time
        self.update_by = update_by
        self.description = description
db.create_all()
db.session.commit()

users = ast.literal_eval(config['DEV_FLASK_CONFIG']['users'])

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@app.route('/')
def entry_page():  # put application's code here
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return redirect(url_for('index_page'))

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

@app.route('/account_list')
def index_page():  # put application's code here
    all_data = Account.query.all()
    return render_template("index.html", accounting=all_data)

# @app.route('/account_list')
# def show_list():
#     return "HI"
#
@app.route('/input/{id}', methods=['GET', 'POST'])
def input_data():
    pass
#
# @app.route('/update/{id}', methods=['PUT', 'POST'])
#
# @app.route('/delete/{id}', methods=['DELETE', 'POST'])






if __name__ == '__main__':
    app.run(host=config['DEV_FLASK_CONFIG']['host'], port=config['DEV_FLASK_CONFIG']['port'])
