#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3

class DBInstance:

#       conn.execute("create table tradelog(id,date,sprice,svolume,scur,bprice,bvilume,vcur)")

        def get(self,STATEMENT):
		conn = sqlite3.connect('tradelog.db')
		cur = conn.cursor()
		result = cur.execute(STATEMENT)
		row = result.fetchone()
		conn.close()
		return row


        def put(self,list):
		conn = sqlite3.connect('tradelog.db')
		cur = conn.cursor()
		result = cur.execute('INSERT INTO logs VALUES(list[0],list[2],list[3],list[4],list[5],list[6],list[7])')
		conn.close()
		return result
