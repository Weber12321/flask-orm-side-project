import pymysql

def connect_database(**kwargs) -> pymysql.connect:
    info = {
        'host': kwargs.get('host'),
        'port': int(kwargs.get('port')),
        'user': kwargs.get('user'),
        'password': kwargs.get('password'),
        'db': kwargs.get('database'),
        'charset': kwargs.get('charset'),
        'cursorclass': pymysql.cursors.DictCursor,
    }
    return pymysql.connect(**info)

