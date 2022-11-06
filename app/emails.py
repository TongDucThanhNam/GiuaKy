from threading import Thread

from flask_mail import Message

from . import mail


def send_async_email(app, message):
    with app.app_context():
        mail.send(message)


def send_email(to, subject, template, **kwargs):
    from flask import current_app
    app = current_app._get_current_object()
    message = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                      sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    from flask import render_template
    message.body = render_template(template + '.txt', **kwargs)
    message.html = render_template(template + '.html', **kwargs)
    print(message)
    thr = Thread(target=send_async_email, args=[app, message])
    thr.start()
    return thr
