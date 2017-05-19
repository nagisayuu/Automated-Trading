#!/usr/bin/env python
# -*- coding:utf-8 -*-

# github
# https://github.com/veox/python2-krakenex

import sys,krakenex

args=sys.argv

if not len(args)==2:
	print("krakenOrder needs 2 arguments [BUY or SELL,volume]")

k = krakenex.API()
k.load_key('../key/kraken.key')

result=k.query_private('AddOrder', {'pair': 'XXBTZEUR',
                                    'type': ''+args[1]+'',
                                    'ordertype': 'market',
                                    'volume': ''+args[2]+''})
print(result)

"""
pair = 資産ペア(ether:XETHZJPY,BTC:XXBTZJPY)
type = 注文のタイプ（買い(buy)／売り(sell?)）
ordertype = 注文のタイプ:
    market(成り行き?)
    limit（price = 指値価格）
    stop-loss（price = ストップロス価格）
    take-profit（price = 利益確定価格）
    stop-loss-profit（price = ストップロス価格, price2 = 利益確定価格）
    stop-loss-profit-limit（price = ストップロス価格, price2 = 利益確定価格）
    stop-loss-limit（price = ストップロストリガ価格, price2 = トリガーが指定された指値価格）
    take-profit-limit（price = 利益確定トリガ価格, price2 = トリガーが指定された指値価格）
    trailing-stop（price = トレーリングストップオフセット）
    trailing-stop-limit（price = トレーリングストップオフセット, price2 = トリガーが指定された指値価格）
    stop-loss-and-limit（price = ストップロス価格, price2 = 指値価格）
price = price（任意、ordertypeに依存）
price2 = 2次価格（任意、ordertypeに依存）
volume = 注文出来高（ロット単位）
leverage = 希望のレバレッジ金額（任意、デフォルト = none)
position = クローズするポジションのTX ID（任意、ポジションをクローズする貯めに使用）
oflags =  注文フラグのリスト（カンマ区切り）（任意）:
    viqc = 見積もり通貨でのボリューム
    plbc = ベース通貨での利益／損失を優先
     nompp = 成行価格保護なし
starttm = スケジュールされたスタート時間（任意）:
    0 = 現在（デフォルト）
    + = スタート時間を現在から  秒後にスケジュール
     = スタート時間のUNIXタイムスタンプ
expiretm = 期限切れの時間（任意）:
    0 = 期限切れなし（デフォルト）
    + = 現在から  秒後に期限切れ
     = 期限切れ時間のUNIXタイムスタンプ
userref = ユーザー参照ID。32ビットの符号つき数字。（任意）
validate = 入力のみを認証する。注文を送信しない（任意）

注文が約定した場合に、クローズ注文をシステムに追加するオプション:
    close[ordertype] = 注文タイプ
    close[price] = 価格
    close[price2] = 2次価格
"""
