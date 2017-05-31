#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

class AlgExecutor:

	def __init__(self):
		# 読み込むファイルの名前
		self.filename=(os.path.dirname(os.path.abspath(__file__)) + '/../../data/201705171720.csv')
		# 現在時刻からここで参照した時間まで遡った時間を対象に処理する(デフォルトは12時間)
		self.refSecond=60*60*12
		self.LIMIT = 30
		self.STOP_LIMIT = 30

	def setFile(self,filename):
		self.filename=filename

	def timefilter(self,data,unixdate):
		import datetime
		# 時刻データを抽出する(デフォルトは指定時刻から12時間前まで)
		refTime=float(unixdate)-self.refSecond
		filtered_data=[x for x in data if x[0] >= refTime]
		return filtered_data

	# 【試験用関数】ローカルファイルから値段の情報を取得
	def readFile(self):
		import common.util as util
		flag,data=util.csv_read(self.filename)
		return data

	# webから値段の情報を取得
	def fetchPrice(self):
		import httplib
		# httpでwebから価格情報を取得
		conn = httplib.HTTPConnection("api.bitcoincharts.com")
		conn.request("GET", "/v1/trades.csv?symbol=coincheckJPY")
		r1 = conn.getresponse()
		body = r1.read()
		data=[[float(elm) for elm in x.split(",")] for x in body.split()]
		return data

	def judgeFromAverage(self,data):
		import numpy as np
		recentPrice=data[0][0]
		del data[0]
		averagePrice=(np.sum(data, axis=0)[0])/len(data)
		if averagePrice<recentPrice:
			if averagePrice+self.LIMIT<recentPrice:
				return "buy"
			else: return "wait"
		else:
			if averagePrice-self.STOP_LIMIT<recentPrice:
				return "wait2"
			else: return "sell"

	def execute(self):
		# 【試験時はコメントアウト】ファイル読み込み
		#data=self.readFile()
		# 【試験時はコメントイン】webから価格情報取得
		data=self.fetchPrice()
		# 売買の判断
		return self.judgeFromAverage(data)
		
