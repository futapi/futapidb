# -*- coding: utf-8 -*-
from flask import Flask, g
# from os import urandom

from .config import sql_host, sql_db, sql_user, sql_pass


# ===    main app    ===
app = Flask(__name__)
app.config.update(
    DEBUG=False,        # debugging to gunicorn
    # SECRET_KEY=urandom(24),
)
# app.jinja_env.line_statement_prefix = '#'

from . import logger  # set logger
from . import controllers  # set controllers

# database
from .models import db


@app.before_request
def before_request():
    g.db = db.connect(sql_host, sql_user, sql_pass, sql_db)


@app.teardown_request
def teardown_request(exception):
    g.db.close()
