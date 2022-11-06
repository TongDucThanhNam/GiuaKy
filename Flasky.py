import os

from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
print("app.config['SQLALCHEMY_DATABASE_URI'] = " + app.config['SQLALCHEMY_DATABASE_URI'])


@app.before_first_request
def create_tables():
    # Nếu database không có gì thì tạo bảng
    print("Run create_tables missing")
    db.create_all()