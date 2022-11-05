import os

from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
print("app.config['SQLALCHEMY_DATABASE_URI'] = " + app.config['SQLALCHEMY_DATABASE_URI'])


@app.before_first_request
def create_tables():
    # Nếu database không có gì thì tạo bảng
    print("Run create_tables")
    db.create_all()

    # lấy các bảng của database "user"
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="user")
    my_cursor = mydb.cursor()
    my_cursor.execute("Show tables")

    # in ra các bảng của database "user"
    for x in my_cursor:
        print(x)

