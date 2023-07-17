from sqlalchemy import create_engine
from sqlalchemy import Integer,String, Column
from sqlalchemy.ext.declarative import declarative_base

ENGINE = create_engine('mysql+mysqldb://root:Kikis_216@localhost:3306/hbtn_0c_0')
BASE = declarative_base()

#create table
class customer(BASE):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key = True)
    name = Column(String(200))
    age = Column(Integer)
    def __str__(self):
        return self.name
    
BASE.metadata.create_all(ENGINE)