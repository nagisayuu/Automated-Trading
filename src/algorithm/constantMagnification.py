#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

class AlgExecuter:

	def __init__(self):
		# 【試験用】読み込むファイルの名前
		self.filename=(os.path.dirname(os.path.abspath(__file__)) + '/../../data/201705171720.csv')
		# 現在時刻からここで参照した時間まで遡った時間を対象に処理する(デフォルトは12時間)
		self.magnification=1.1

	def setFile(self,filename):
		self.filename=filename

	def setMagnification(self,magnification):
		self.magnification=magnification

	# 【試験用関数】ローカルファイルから値段の情報を取得
	def readFile(self):
		import common.util as util
		data=util.csv_read(self.filename)
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

	def checkFlag(self):
		import os
		directory=os.path.dirname(os.path.abspath(__file__))
		flagFile=name = os.path.normpath(os.path.join(directory, '../../flag/constantMagnification.flag'))
		return os.path.isfile(flagFile)

	def execute(self):
		import common.util as util
		# フラグファイルパス
		directory=os.path.dirname(os.path.abspath(__file__))
                path=os.path.normpath(os.path.join(directory, '../../flag/constantMagnification.flag'))

	# 1.現在の価格を取得
		# 【試験時はコメントアウト】ファイル読み込み
		#data=self.readFile()
		# 【試験時はコメントイン】webから価格情報取
		recData=self.fetchPrice()

	# 2.今etherを持っているかどうか確認する。取引用のフラグファイルを探す
		flag=util.checkFlag(path)

	# 3.フラグファイルがなかったら買う(DBに情報入れる)(処理終了) フラグファイルを作成。	
		if not flag:
			util.csv_write(path,[recData[0]])
			return "buy",recData
	# 4.フラグファイルがあったらファイルから購入時の価格を取得
		else:
			fileData=util.csv_read(path)

	# 5.現在の価格が購入時より閾値以上高かったら売却(DBに情報入れる) フラグファイルを削除
		if fileData[0][0]*self.magnification < recData:
			util.remFile(path)
			return "sell",recData
	# 6.現在の価格よりも低かったらstay(何もしない)
		else:
			return "wait",[]
