from app import db


class User(db.Model):
    __tablename__ = 'users'
    userName = db.Column(db.String(64), primary_key=True)
    password = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    email = db.Column(db.String(64))
    balance = db.Column(db.Integer)
    tradeHistoryCode = db.Column(db.String(64))

    def __int__(self, userName, password, phone, email, balance, tradeHistoryCode):
        self.userName = userName
        self.password = password
        self.phone = phone
        self.email = email
        self.balance = balance
        self.tradeHistoryCode = tradeHistoryCode

    def verify_password(self, password):
        return self.password == password

    def __repr__(self):
        return '<User %r>' % self.userName

class TransactionHistory(db.Model):
    __tablename__ = 'transactionHistory'
    transactionHistoryCode = db.Column(db.String(64), primary_key=True)
    dayTrade = db.Column(db.String(64))
    transactionAmount = db.Column(db.Integer)
    balanceAfterTransaction = db.Column(db.Integer)
    content = db.Column(db.String(64))


class SchoolFee(db.Model):
    __tablename__ = 'schoolFee'
    mssv = db.Column(db.String(64), primary_key=True)
    hoTen = db.Column(db.String(64))
    soTien = db.Column(db.Integer)
