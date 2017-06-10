#!/usr/bin/env python
# -*- coding:utf-8 -*-

# src/をパスに追加
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from datetime import datetime as dt
import krakenex as api
import common.util as util
# -- シミュレータのみ追加 ローカルファイルからデータを読み込む関数
import interface.localfile.getRecord as gr

# ユーザ情報、仮想通貨情報の入力
pair = 'XETHZJPY'
keyFile = '../../key/touei.key.test'

# 仮想通貨の購入または売却の可否を決定
import algorithm.constantMagnification as alg

algexecutor = alg.AlgExecutor(pair, keyFile)

# -- シミュレータのみ追加 データ取得関数をローカルから読み込むものへ変更
stub = gr.Interface("data/coincheckJPY.csv")
algexecutor.fetchPrice = stub.fetchCurrentPrice

# -- シミュレータのみ追加 結果書き込みパスを追加
curdir = os.path.dirname(os.path.abspath(__file__))
resultFile = os.path.join(curdir, '../../data/constantMagnification.result')

# -- シミュレータのみ追加 グラフ描画用のフラグ
flagvaluable = 0

def executeLogic():


    # buy,sell,waitをアルゴリズムに従って決定
    result, recData = algexecutor.execute()

    # 仮想通貨の購入または売却
    if result == "wait":

        # -- シミュレータのみ追加 ローカルファイルに購入情報を記載
        util.csv_write(resultFile, [[recData["time"], recData["price"], 0, flagvaluable]], "a+")

    else:
        date = dt.now().strftime('%s')
        # dbi=pgm.DBInstance()
        k = api.API()
        k.load_key(keyFile)
        directory = os.path.dirname(os.path.abspath(__file__))
        path = os.path.normpath(os.path.join(directory, '../../flag/constantMagnification.flag'))
        if result == "buy":
            # 購入可能数を取得
            ## 資産を取得
            asset = k.query_private('Balance', {})["result"]["ZJPY"]
            ## 購入可能数を計算
            volume = float(asset) / float(recData["price"])

            # 購入
            # response=k.query_private('AddOrder', {'pair': pair,'type': result,'ordertype': 'market','volume': volume})

            # ローカルファイルに購入情報を記載
            util.csv_write(path, [[recData["price"], volume]])

            # -- シミュレータのみ追加 ローカルファイルに購入情報を記載
            flagval = flagval + 1
            util.csv_write(resultFile, [[recData["time"], recData["price"], volume, flagvaluable]], "a+")

            # DBに購入情報を挿入
            # dbi.put(response[0],date,"-","-","JPY",recData["price"],volume,"ETH")

        else:
            # 売却可能数を取得
            flag, data = util.csv_read(path)
            volume = data[0][1]

            # 売却
            # response=k.query_private('AddOrder', {'pair': pair,'type': result,'ordertype': 'market','volume': volume})

            # ローカルファイルを削除
            util.remFile(path)

            # -- シミュレータのみ追加 ローカルファイルに購入情報を記載
            flagval = flagval - 1
            util.csv_write(resultFile, [[recData["time"], recData["price"], volume, flagvaluable]], "a+")

            # DBに売却情報を挿入
            # dbi.put(response[0],date,recData["price"],volume,"ETH","-","-","JPY")


def constantMagnification():
    # -- シミュレータのみ追加 反復実行
    for i in range(0, 10):
        executeLogic()


if __name__ == "__main__":
    constantMagnification()
