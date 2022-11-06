from random import randint

from flask import render_template, url_for, redirect
from flask_login import login_required, current_user

from app import db
from app.transaction import transaction
from app.transaction.forms import TransactionForm, OtpForm
from ..emails import send_email
from ..models import SchoolFee, TransactionProcessing


# Trang đóng học phí
@login_required
@transaction.route('/', methods=['GET', 'POST'])
def DongHocPhi():
    print("transaction")
    form = TransactionForm()

    schoolfees = get_schoolfee_data()
    print(current_user.userName)
    print(current_user.balance)
    print(current_user.email)

    if form.validate_on_submit():
        schoolFee = SchoolFee.query.filter_by(mssv=form.mssv.data).first()
        if schoolFee is None:
            print("Sinh viên không nợ hoc phí hoặc không có trong CSDL")
        else:
            transactionProcessing = TransactionProcessing(
                userId=current_user.userId,
                transactionTime="19/05/2002",
                transactionHistoryCode=current_user.tradeHistoryCode
            )

            db.session.add(transactionProcessing)
            db.session.commit()
            return redirect(location=url_for('transaction.guiOTP'),)
        #

    return render_template('transaction.html', form=form, schoolfees=schoolfees)


def createOTP():
    return randint(1000, 9999)


@transaction.route('/otp', methods=['GET', 'POST'])
def guiOTP():
    user = current_user
    email_subject = "Confirm transaction"
    print("Email send")
    otp = createOTP()
    form = OtpForm()

    send_email(user.email, email_subject, 'mail/otp', user=user, otp=otp)
    print("Hàm gửi OTP")
    if form.validate_on_submit():
        print(otp)
        print(form.otp.data)
        if form.otp.data == otp:
            # Xoa sv no hoc phi
            print("OTP confirm success")
            redirect(location=url_for('main.index'))
    return render_template('otp.html', form=form)


def get_schoolfee_data():
    return SchoolFee.query.all()
