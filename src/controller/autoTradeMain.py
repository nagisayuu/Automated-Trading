#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
# src/をパスに追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')


def main():
	# ユーザ情報、仮想通貨情報の入力
	
	# 仮想通貨の購入または売却の可否を決定
	import algorithm.thresholdSetting as alg
	algexecuter=alg.AlgExecuter()
	result=algexecuter.execute()
	# 仮想通貨の購入または売却
	if result=="wait":
		return 0

	import krakenex
	k = krakenex.API()
	k.load_key('../../key/kraken.key')
	response=k.query_private('AddOrder', {'pair': 'XXBTZEUR','type': 'buy','ordertype': 'market','volume': '1'})
	print(response)


if __name__ == "__main__":
	main()
