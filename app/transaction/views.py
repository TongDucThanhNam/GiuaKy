import datetime
from random import randint

from flask import render_template, url_for, redirect
from flask_login import login_required, current_user

from app import db
from app.transaction import transaction
from app.transaction.forms import TransactionForm, OtpForm
from ..emails import send_email
from ..models import SchoolFee, TransactionProcessing, OtpManagement, User


# Trang đóng học phí
@login_required
@transaction.route('/', methods=['GET', 'POST'])
def DongHocPhi():
    print("transaction")
    form = TransactionForm()
    schoolfees = get_schoolfee_data()
    user = current_user
    email_subject = "Confirm transaction"

    if form.validate_on_submit():
        # Check MSSV dang duoc thanh toan Or tai khoan dang thanh toan o mot noi khac
        user = User.query.filter_by(userName="admin").first()
        user_trans_check = TransactionProcessing.query.filter_by(userId=current_user.userId).first()
        if user_trans_check is not None:
            print("User dang thuc hien mot giao dich khac")
            return redirect(url_for('transaction.DongHocPhi'))
        mssv_trans_check = TransactionProcessing.query.filter_by(mssv=form.mssv.data).first()
        if mssv_trans_check is not None:
            print("Hoc phi cua sinh vien nay dang duoc thanh toan")
            return redirect(url_for('transaction.DongHocPhi'))

        schoolFee = SchoolFee.query.filter_by(mssv=form.mssv.data).first()
        if schoolFee is None:
            print("Sinh viên không nợ hoc phí hoặc không có trong CSDL")
        else:
            if current_user.balance < int(form.soTien.data):
                print("Khong du so du")
                return redirect(url_for('transaction.DongHocPhi'))

            # balance are OK
            transactionProcessing = TransactionProcessing(
                userId=current_user.userId,
                mssv=schoolFee.mssv,
                transactionTime=datetime.datetime.now().strftime('%H:%M:%S %Y-%m-%d'),
                transactionHistoryCode=current_user.tradeHistoryCode
            )
            db.session.add(transactionProcessing)

            otp = createOTP()
            token = createToken()
            otpManagement = OtpManagement(
                otp=otp,
                token=token,
                time_send=datetime.datetime.now().strftime('%H:%M:%S %Y-%m-%d')
            )
            db.session.add(otpManagement)

            # db commit
            db.session.commit()

            send_email(user.email, email_subject, 'mail/otp', user=user, otp=otp)
            return redirect(
                location=url_for('transaction.guiOTP', token=token, mssv=form.mssv.data))
        #

    return render_template('transaction.html', form=form, schoolfees=schoolfees)


def createToken():
    return randint(1000, 9999)


def createOTP():
    return randint(1000, 9999)


@transaction.route('/otp/<token>/<mssv>', methods=['GET', 'POST'])
def guiOTP(token, mssv):
    print("Hàm gửi OTP")
    form = OtpForm()
    # check otp
    otp = OtpManagement.query.filter_by(token=token).first()

    if form.validate_on_submit():
        print("OTP is", otp.getOTP())
        print("Data is", form.otp.data)
        if int(form.otp.data) == int(otp.getOTP()):
            # Tru tien vao so du
            new_balance = current_user.balance - SchoolFee.query.filter_by(mssv=mssv).first().get_soTien()
            user_after_transaction = User.query.filter_by(userId=current_user.userId).first()
            user_after_transaction.balance = new_balance

            # Xoa sv no hoc phi
            SchoolFee.query.filter_by(mssv=mssv).delete()
            # Hoan tat Transaction => Xoa khoi bang TransactionProcessing
            TransactionProcessing.query.filter_by(
                mssv=mssv).delete()
            # Xoa OTP management
            OtpManagement.query.filter_by(token=token).delete()

            db.session.commit()

            print("OTP confirm success")
            # Quay lai trang transaction
            return redirect(url_for('transaction.DongHocPhi'))
        else:
            print("Ma OTP khong trung khop")
            # Giao dich khong thanh cong => Xoa khoi bang TransactionProcessing
            TransactionProcessing.query.filter_by(
                mssv=mssv).delete()
            # Xoa OTP management
            OtpManagement.query.filter_by(token=token).delete()

            db.session.commit()

            return redirect(url_for('transaction.DongHocPhi'))

    return render_template('otp.html', form=form)


def get_schoolfee_data():
    return SchoolFee.query.all()
