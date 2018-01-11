# -*- coding: utf-8 -*-
import torndb


def connect(sql_host, sql_user, sql_pass, sql_db):
    return torndb.Connection(sql_host, sql_db, sql_user, sql_pass)


def getPrices(item_id, platform=None):
    # get sorted data, return ordered (3.6+ default) dict
    pass
