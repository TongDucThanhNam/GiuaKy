from flask import render_template, flash, redirect, url_for

from app.main import main
from app.main.forms import LoginForm
from app.transaction.forms import TransactionForm

from ..models import User
from flask_login import login_user


# Trang chủ
@main.route('/', methods=['GET', 'POST'])
def index():
    print("Trang chủ")
    form = TransactionForm()
    return render_template('index.html', form=form)


# Trang đăng nhập
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userName=form.userName.data).first()
        if user is not None and user.verify_password(form.password.data):
            print("Login success")
            login_user(user=user)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)
