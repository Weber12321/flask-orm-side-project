import configparser
from flask import Flask



app = Flask(__name__)


@app.route('/index')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/account_list')
def show_list():
    pass

@app.route('/input/{id}')
def input_data():
    pass





if __name__ == '__main__':
    app.run()
