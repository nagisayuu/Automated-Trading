#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys, linecache

# ローカルファイルから取得する関数を定義したライブラリ
class Interface:
    def __init__(self, path):
        self.index = 1
        self.path = path

    # 現在の価格を取得するAPI
    # arg なし
    # ret1 TF
    # ret2 [取得時刻,現在の価格(直近3取引の価格の平均)](成功) , エラーメッセージを含むリスト(失敗)
    def fetchCurrentPrice(self):
        sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../')
        target_line = linecache.getline(self.path, self.index)
        data = target_line.split(",")
        linecache.clearcache()
        self.index = self.index + 1
        return True, {"time": data[0], "price": data[1]}
