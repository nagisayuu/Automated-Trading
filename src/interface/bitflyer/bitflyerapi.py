#!/usr/bin/env python
# -*- coding:utf-8 -*-

import krakenex

# krakenから取得する関数を定義したライブラリ
class Interface:

    def __init__(self,pair,filename):
        self.pair=pair
        ### About pair
        # XETHZJPY : ethereum - JPY
        self.api=krakenex.API()
        self.api.load_key(filename)

    # 直近の取引情報を取得するAPI
    # arg なし
    # ret1 TF
    # ret2 取引情報を含んだ配列
    def getTradeData(self):
        response=self.api.query_public('Trades', {'pair': self.pair})
        if len(response["error"]) == 0:
            return True,response
        else:
            return False,response

    # 現在の価格を取得するAPI
    # arg なし
    # ret1 TF
    # ret2 [取得時刻,現在の価格(直近3取引の価格の平均)](成功) , エラーメッセージを含むリスト(失敗)
    def fetchCurrentPrice(self):
        tf,response=self.getTradeData()
        if tf == False:
            return False,{error: response["error"]}
        tradesNum=3
        datalen=len(response["result"][self.pair])
        priceSum=0
        for j in [datalen-i for i in range(tradesNum)]:
            priceSum=priceSum+float(response["result"][self.pair][j-1][0])
        return True,{"time": response["result"][self.pair][datalen-1][2],"price": priceSum/tradesNum}

    # アカウントの資産の量を取得するAPI
    # arg 対象とする資産
    # ret1 TF
    # ret2 現在の資産 , エラーメッセージ
    def getAsset(self,currency):
        ### About currency
        # ZJPY : JPY
        response = self.api.query_private('Balance', {})
        if len(response["error"]) == 0:
            return True,response["result"][currency]
        else:
            return False,response["error"]

    # 取引を発注するAPI
    # arg1 買い(buy)注文または売り(sell)注文
    # arg2 発注量
    # ret1 TF
    # ret2 現在の資産 , エラーメッセージ
    def order(self,sbtype,result):
        response = self.api.query_private('AddOrder', {'pair': self.pair,'type': sbtype,'ordertype': 'market','volume': volume})
        if len(response["error"]) == 0:
            return True,response
        else:
            return False,response
