#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys

class AlgExecutor:

	def __init__(self,pair,keyFile):
		# 【試験用】読み込むファイルの名前
		self.filename=(os.path.dirname(os.path.abspath(__file__)) + '/../../data/201705171720.csv')
		# 現在時刻からここで参照した時間まで遡った時間を対象に処理する(デフォルトは12時間)
		self.magnification=1.1
		self.pair=pair
		self.keyFile=keyFile

	# 【試験用】オブジェクトの読み込みファイル名を設定
	# arg ファイル名
	# ret なし
	def setFile(self,filename):
		self.filename=filename

	def setMagnification(self,magnification):
		self.magnification=magnification

	# webから値段の情報を取得
	def fetchPrice(self):
		srcpath=os.path.dirname(os.path.abspath(__file__)) + '/../'
		if not srcpath in sys.path:
			sys.path.append(srcpath)
			appendFlag=True
		import interface.kraken.krakenAPI as kraken
		api=kraken.Interface(self.pair,self.keyFile)
		flag,data=api.fetchCurrentPrice()
		if appendFlag==True:
			sys.path.remove(srcpath)
		return flag,data

	# ローカルファイルの存在を確認
	# arg なし
	# ret TF
	def checkFlag(self):
		import os
		directory=os.path.dirname(os.path.abspath(__file__))
		flagFile=name = os.path.normpath(os.path.join(directory, '../../flag/constantMagnification.flag'))
		return os.path.isfile(flagFile)

	# アルゴリズムを実行
	# arg なし
	# ret1 買い("sell")か売り("buy")
	# ret2 {値段("price")、時刻("time"}を要素にもつリスト
	def execute(self):
		import common.util as util
		# フラグファイルパス
		directory=os.path.dirname(os.path.abspath(__file__))
                path=os.path.normpath(os.path.join(directory, '../../flag/constantMagnification.flag'))

	# 1.現在の価格を取得
		# 【試験時はコメントアウト】ファイル読み込み
		#flag,data=util.csv_read(path)
		# 【試験時はコメントイン】webから価格情報取
		flag,recData=self.fetchPrice()
		if not flag:
			return "wait",recData
	# 2.今etherを持っているかどうか確認する。取引用のフラグファイルを探す
		flag=util.checkFlag(path)

	# 3.フラグファイルがなかったら買う(DBに情報入れる)(処理終了) フラグファイルを作成。	
		if not flag:
			# util.csv_write(path,[recData[0]])
			return "buy",recData
	# 4.フラグファイルがあったらファイルから購入時の価格を取得
		else:
			flag,fileData=util.csv_read(path)

	# 5.現在の価格が購入時より閾値以上高かったら売却(DBに情報入れる) フラグファイルを削除
		if fileData[0][0]*self.magnification < recData["price"]:
			# util.remFile(path)
			return "sell",recData
	# 6.現在の価格よりも低かったらstay(何もしない)
		else:
			return "wait",[]
