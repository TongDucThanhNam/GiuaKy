from flask import render_template, flash, redirect, url_for

from app.main import main
from app.main.forms import LoginForm
from ..models import User


# Trang chủ
@main.route('/', methods=['GET', 'POST'])
def index():
    print("Trang chủ")
    return render_template('index.html')


# Trang đăng nhập
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userName=form.userName.data).first()
        if user is not None and user.verify_password(form.password.data):
            print("Login success")
            return redirect(url_for('transaction.DongHocPhi'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)
