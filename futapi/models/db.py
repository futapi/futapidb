# -*- coding: utf-8 -*-
import torndb


def connect(sql_host, sql_user, sql_pass, sql_db):
    return torndb.Connection(sql_host, sql_db, sql_user, sql_pass)
