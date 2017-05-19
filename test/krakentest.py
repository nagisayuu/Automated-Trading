#!/usr/bin/env python
# -*- coding:utf-8 -*-

import krakenex

def add(x, y):
    print x + y

add(1,2)

k = krakenex.API('SIJa3QJSDXmGGBQOLH+6YhW1fwt3J4Sdiefw+ysc/jg406EkqyoSiXo4','dHHIlxpExe/cP/kQ2wKIZ5vcSPX3cZNiWQYdA9+mjkyLTpr3XdIC8dUi/3yJRYArFe/+jSFlyP62nDnfEyB8cA==')

#資産情報の表示
assets = k.query_private('Assets')['error']
print assets




#total_balance = k.query_private('TradeBalance', {'asset':'ZJPY'})['result']['tb']
#print total_balance

ticks = k.query_public('Ticker',{'pair':'XXBTZJPY,ETHXBT,ETHJPY'})['result']
print ticks["XXBTZJPY"]
