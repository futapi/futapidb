# -*- coding: utf-8 -*-
from flask import render_template, request, make_response

from ..deploy import app

# models
from ..models import db


@app.route('/db/prices/<int:item_id>', methods=['GET'])
@app.route('/db/prices', methods=['GET', 'POST'])
def dbPrices(platform=None, item_id=None, price1=None, price2=None, price3=None, date=None):
    if request.method == 'POST':
        # validate params, add to db
        pass
    elif request.method == 'GET' and item_id:
        # validate item_id
        data = db.getPrices(item_id)
        prepare response
        pass
    else:
        # invalid request
        pass
