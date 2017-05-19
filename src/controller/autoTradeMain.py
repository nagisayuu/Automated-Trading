#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
# src/をパスに追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')


def main():
	# ユーザ情報、仮想通貨情報の入力
	
	# 売買の可否決定に必要な情報の取得
	# →algorithmモジュールの中で実装することにしたので本箇所では記載不要
	# 仮想通貨の購入または売却の可否を決定
	import algorithm.thresholdSetting as alg
	algexecuter=alg.AlgExecuter()
	algexecuter.execute()
	#VCInfo = getVCInfo()
	#orderInfo = calcVCInfo(VCInfo)
	# 仮想通貨の購入または売却
	#k.query_private('AddOrder', {'pair': 'XXBTZEUR',
        #                     'type': 'buy',
        #                     'ordertype': 'limit',
        #                     'price': '1',
        #                     'volume': '1',
        #                     'close[pair]': 'XXBTZEUR',
        #                     'close[type]': 'sell',
        #                     'close[ordertype]': 'limit',
        #                     'close[price]': '9001',
        #                     'close[volume]': '1'})

#k = krakenex.API()
#k.loadkey('kraken.key')

if __name__ == "__main__":
	main()
