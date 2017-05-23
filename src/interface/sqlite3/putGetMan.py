#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3

class DBInstance:

#       conn.execute("create table tradelog(id,date,sprice,svolume,scur,bprice,bvilume,vcur)")

        def get(self,STATEMENT):
		conn = sqlite3.connect('tradelog.db')
		cur = conn.cursor()
		result = cur.execute(STATEMENT)
		conn.close()
		
		return result

#最新の情報を含む一行から

        def put():
