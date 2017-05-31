#!/usr/bin/env python
# -*- coding:utf-8 -*-

# csvファイル読み込み関数
# arg1 ファイル名(パス)
# ret1 0(成功) or 1(失敗)
# ret2 csvを読み込んだリスト(成功) or エラーメッセージを含んだリスト(失敗)
def csv_read(filename):
    import csv
    try:
        with open(filename, 'r') as fd:
            data=[[float(elm) for elm in v] for v in csv.reader(fd)]
        return 0,data
    except Exception as e:
        print '=== エラー内容 ==='
        print 'type:' + str(type(e))
        print 'args:' + str(e.args)
        print 'message:' + e.message
        return 1,['read csv failed']

# csvファイル作成関数
# arg1 ファイル名(パス)
# arg2 csvの情報を格納した配列
# ret1 0(成功) or 1(失敗)
def csv_write(filename,csvlist):
    import csv
    try:
        with open(filename, 'w') as fd:
            csvWriter = csv.writer(fd)
            csvWriter.writerows(csvlist)
        return 0
    except Exception as e:
        print '=== エラー内容 ==='
        print 'type:' + str(type(e))
        print 'args:' + str(e.args)
        print 'message:' + e.message
        return 1

# ファイル存在確認関数
# arg1 ファイル名(パス)
# ret True(存在) False(存在しない)
def checkFlag(path):
    import os
    return os.path.isfile(path)

# ファイル削除関数
# arg1 ファイル名(パス)
# ret 0(成功) 1(失敗)
def remFile(path):
    import os
    try:
        os.remove(path)
        return 0
    except Exception as e:
        print '=== エラー内容 ==='
        print 'type:' + str(type(e))
        print 'args:' + str(e.args)
        print 'message:' + e.message
        return 1
