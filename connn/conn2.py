from sqlalchemy import create_engine

DB_URL = 'mysql+mysqldb://root:Kikis_216@localhost:3306/hbtn_0c_0'
ENGINE = create_engine(DB_URL)

cursor = ENGINE.connect()
query = 'select * from first_table;'
result = cursor.execute(query)
for i in result:
    print('id : {}'.format(i[0]))
    print('name : {}'.format(i[1]))