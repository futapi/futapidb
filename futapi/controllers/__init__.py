# -*- coding: utf-8 -*-
from flask import redirect, url_for

from ..deploy import app

# models
# from ..models import user

# controllers
from . import error  # error controller
# from . import api    # api controller


# ===    routes    ===
@app.route('/index.html')
@app.route('/index')
@app.route('/')
def index():
    return redirect('https://github.com/futapi/fut')
