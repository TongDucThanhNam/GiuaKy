from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Form đóng học phí
class TransactionForm(FlaskForm):
    mssv = StringField('MSSV', validators=[DataRequired()])
    hoTen = StringField('Ho Ten')
    soTien = StringField('So Tien', validators=[DataRequired()])
    submit = SubmitField('Submit')


class OtpForm(FlaskForm):
    otp = StringField('OTP', validators=[DataRequired()])
    submit = SubmitField('OTP Submit')
