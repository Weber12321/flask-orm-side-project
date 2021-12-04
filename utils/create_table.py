from datetime import  datetime
from sqlalchemy import create_engine, MetaData, Table, \
    Column, Integer, String, Date, DateTime, inspect


def create_table_if_not_exist(database_connection_info: str) -> None:
    engine = create_engine(database_connection_info)

    if not inspect(engine).has_table('account'):
        meta = MetaData()

        accounting = Table(
            'account', meta,
            Column('id', Integer, primary_key=True),
            Column('items', String(30), nullable=False),
            Column('date_info', Date, nullable=False),
            Column('amount', Integer, nullable=False),
            Column('payment', String(30), nullable=False),
            Column('card', String(30), nullable=True),
            Column('status', String(30), nullable=False),
            Column('purpose', String(100), nullable=False),
            Column('insert_time', DateTime, default=datetime.now),
            Column('insert_by', String(30), default='Weber'),
            Column('update_time', DateTime, onupdate=datetime.now, default=datetime.now),
            Column('update_by', String(30), nullable=True),
            Column('description', String(300), nullable=True)
        )

        meta.create_all(engine)

