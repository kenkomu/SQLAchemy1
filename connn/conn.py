from sqlalchemy import create_engine

DB_URL = 'mysql+mysqldb://root:Kikis_216@localhost:3306/sys'

ENGINE = create_engine(DB_URL)

conn = ENGINE.connect()

try:
    print("your connection ok \n connection object is: {}".format(conn))
except:
    print("your conn is not connected")