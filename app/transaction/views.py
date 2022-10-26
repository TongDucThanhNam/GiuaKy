from flask import render_template

from app.transaction import transaction
from app.transaction.forms import TransactionForm


# Trang đóng học phí
@transaction.route('/', methods=['GET', 'POST'])
def DongHocPhi():
    print("transaction")
    form = TransactionForm()
    return render_template('transaction.html', form=form)
