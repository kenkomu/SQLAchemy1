from conn3 import customer, ENGINE
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=ENGINE)
session = Session()

name = input('enter your name:')
age = input('enter your age:')

cust1  = customer(customer_name=name, customer_age= age)
session.add(cust1)
session.commit()
print('details are inserted')
