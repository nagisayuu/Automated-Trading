#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3

class DBInstance:

        def __init__(self):
                conn = sqlite3.connect(tradelog.db)
                conn.execute("create table tradelog(id,date,sprice,svolume,scur,bprice,bvilume,vcur)")

        def get():


        def put():
