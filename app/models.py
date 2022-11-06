from flask_login import UserMixin

from app import db, login


@login.user_loader
def load_user(userId):
    return User.query.get(userId)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64))
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

    # flask_login
    def get_id(self):
        return self.userId

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
    # remove content later
    content = db.Column(db.String(64))

    def get_id(self):
        return self.transactionHistoryCode


class SchoolFee(db.Model):
    __tablename__ = 'schoolFee'
    mssv = db.Column(db.Integer, primary_key=True)
    hoTen = db.Column(db.String(64))
    soTien = db.Column(db.Integer)

    def get_id(self):
        return self.mssv

    def get_soTien(self):
        return self.soTien


# Khi tạo bấm thanh toán, sẽ tạo ra đối tượng TransactionProcessing lưu thông tin.
class TransactionProcessing(db.Model):
    __tablename__ = 'transactionProcessing'
    transactionProcessingCode = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    mssv = db.Column(db.Integer)
    transactionHistoryCode = db.Column(db.String(64))
    transactionTime = db.Column(db.String(64))

    def get_id(self):
        return self.transactionProcessingCode


class OtpManagement(db.Model):
    otpId = db.Column(db.Integer, primary_key=True)
    otp = db.Column(db.Integer)
    token = db.Column(db.Integer)
    time_send = db.Column(db.String(64))

    def get_id(self):
        return self.otpId
    def getOTP(self):
        return self.otp