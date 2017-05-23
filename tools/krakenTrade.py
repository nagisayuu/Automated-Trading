#!/usr/bin/env python
# -*- coding:utf-8 -*-

# github
# https://github.com/veox/python2-krakenex

import sys,krakenex

args=sys.argv

if not len(args)==1:
	print("krakenTrades needs no arguments")
	sys.exit(1)

k = krakenex.API()
k.load_key('../key/kraken.key')

result=k.query_private('TradesHistory', {'start': '1495265581'})
print(result)



"""
type = 取引のタイプ（任意）
    all = すべてのタイプ（デフォルト）
    any position = すべてのポジション（オープンまたはクローズ）
    closed position = クローズされたポジション
    closing position = ポジションの全部または一部をクローズする任意の取引
    no position = ポジションを伴わない取引
trades = ポジションに関連する取引を出力に含めるかどうか（任意、デフォルト = false）
start = 開始時のUNIXタイムスタンプ、または取引TX ID発行時（任意、エクスクルーシブ）
end = 終了時のUNIXタイムスタンプ、または取引TX ID発行時（任意、インクルーシブ）
ofs = 結果オフセット
"""
