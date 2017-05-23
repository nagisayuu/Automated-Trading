#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
# src/をパスに追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')


def main():
	# ユーザ情報、仮想通貨情報の入力
	
	# 仮想通貨の購入または売却の可否を決定
	import algorithm.constantMagnification as alg
	algexecuter=alg.AlgExecuter()
	# buy,sell,waitをアルゴリズムに従って決定
	result,recData=algexecuter.execute()
	# 仮想通貨の購入または売却
	if result=="wait":
		return 0
	else:
		import krakenex,common.util as util
		import interface.sqlite3.putGetMan as pgm
		import datetime.datetime as dt
		date=dt.now().strftime('%s')
		dbi=pgm.DBInstance()
		k = krakenex.API()
		k.load_key('../../key/kraken.key')
		path=os.path.normpath(os.path.join(directory, '../../flag/constantMagnification.flag'))
		if result=="buy":
			# 購入可能数を取得
			## 資産を取得
			asset=k.query_private('Balance', {})["result"]["ZJPY"]
			## 購入可能数を計算
			volume=asset/recData[0][0]
			# 購入
			response=k.query_private('AddOrder', {'pair': 'XETHZJPY','type': result,'ordertype': 'market','volume': volume})
			# ローカルファイルに購入情報を記載
			util.csv_write(path,[recData[0][0],volume])
			# DBに購入情報を挿入
			dbi.put(response[0],date,"-","-","JPY",recData[0][0],volume,"ETH")
		else:
			# 売却可能数を取得
			volume=util.csv_read(path)[0][0]
			# 売却
			response=k.query_private('AddOrder', {'pair': 'XETHZJPY','type': result,'ordertype': 'market','volume': volume})
			# ローカルファイルを削除
			util.remFile(path)
			# DBに売却情報を挿入
			dbi.put(response[0],date,recData[0][0],volume,"ETH","-","-","JPY")

if __name__ == "__main__":
	main()
