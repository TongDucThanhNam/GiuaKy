from flask import render_template
from flask_login import login_required, current_user

from app import db
from app.transaction import transaction
from app.transaction.forms import TransactionForm
from ..models import SchoolFee, TransactionProcessing


# Trang đóng học phí
@login_required
@transaction.route('/', methods=['GET', 'POST'])
def DongHocPhi():
    print("transaction")
    form = TransactionForm()
    print(current_user.userName)
    print(current_user.balance)

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

        #

    return render_template('transaction.html', form=form)


def get_tuition(form):
    tuition = SchoolFee.query.filter_by(mssv=form.mssv.data)
    return tuition.soTien
