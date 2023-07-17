from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import mapper

DB_URL = 'mysql+mysqldb://root:Kikis_216@localhost:3306/hbtn_0c_0'
ENGINE = create_engine(DB_URL)

metadata = MetaData()

user = Table ('user', metadata,
              Column('id', Integer, primary_key= True),
              Column('name', String(50)),
              Column('password', String(50))
              )

class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password

mapper(User, user)
metadata.create_all(ENGINE)
