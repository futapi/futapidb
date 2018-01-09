# -*- coding: utf-8 -*-
import logging

from .deploy import app
from .config import log_file, email_admin, email_sender, smtp_user, smtp_passwd


# set file handler
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s [%(levelname)s] [%(name)s] %(funcName)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.DEBUG)


# set email handler
email_handler = logging.handlers.SMTPHandler(
    '127.0.0.1',
    email_sender['email'],
    email_admin['email'],
    'futapi.tk: ERROR',
    credentials=(smtp_user, smtp_passwd)
)
email_handler.setFormatter(logging.Formatter('''
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Function:           %(funcName)s
Time:               %(asctime)s

Message:

%(message)s
'''))
# email_handler.setLevel(logging.ERROR)
email_handler.setLevel(logging.DEBUG)


# attach handlers to logger
app.logger.addHandler(file_handler)
app.logger.addHandler(email_handler)
app.logger.setLevel(logging.DEBUG)
