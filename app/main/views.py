from flask import render_template, flash, redirect, url_for

from app.main import main
from app.main.forms import LoginForm
from app.transaction.forms import TransactionForm

from ..models import User, SchoolFee
from flask_login import login_user, login_required, logout_user


# Trang chủ
@main.route('/', methods=['GET', 'POST'])
def index():
    print("Trang chủ")
    schoolFees = get_all_schoolfee()
    for schoolFee in schoolFees:
        print(schoolFee.hoTen)
    return render_template('index.html', schoolFees=schoolFees)


# Trang đăng nhập
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userName=form.userName.data).first()
        if user is not None and user.verify_password(form.password.data):
            print("Login success")
            login_user(user=user)
            return redirect(url_for('transaction.DongHocPhi'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)


def get_all_schoolfee():
    return SchoolFee.query.all()


@main.route("/logout")
@login_required
def log_out():
    logout_user()
    return redirect(url_for('main.index'))
