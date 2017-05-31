#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os,re,unittest
# 対象ファイルをパスに追加(srcディレクトリとtestディテク鳥がで追加するため手動設定の必要なし)
rootDir=re.sub(r'/test/.*','',os.path.dirname(os.path.abspath(__file__)))
targetFile=rootDir+'/src'+re.sub(rootDir+'/test','',os.path.dirname(os.path.abspath(__file__)))+'.py'
targetDir=os.path.dirname(targetFile)

sys.path.append(targetDir)

import util
class unittestMain(unittest.TestCase):
    """あるクラスをテストするテストクラス"""
    CLS_VAL = 'none'

    # テストクラスが初期化される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def setUpClass(cls):
        if sys.flags.debug: print('> setUpClass method is called.')
        # テストの準備するための重い処理のメソッドを実行
        cls.CLS_VAL = '> setUpClass : initialized!'
        if sys.flags.debug: print(cls.CLS_VAL)

    # テストクラスが解放される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def tearDownClass(cls):
        if sys.flags.debug: print('> tearDownClass method is called.')
        # setUpClassで準備したオブジェクトを解放する
        cls.CLS_VAL = '> tearDownClass : released!'
        if sys.flags.debug: print(cls.CLS_VAL)

    # テストメソッドを実行するたびに呼ばれる
    def setUp(self):
        if sys.flags.debug: print(os.linesep + '> setUp method is called.')
        # テストの準備をするための軽い処理を実行
        self.target = util

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        if sys.flags.debug: print(os.linesep + '> tearDown method is called.')
        # setUpで準備したオブジェクトを解放する
        del(self.target)

    def test_checkFlag(self):
        # Success prepare
        import subprocess
        mvFlag = False
        curdir=os.path.dirname(os.path.abspath(__file__))
        flagFile = os.path.join(curdir, '../../../flag/constantMagnification.flag')
        if os.path.isfile(flagFile):
            cmd="mv "+flagFile+" /tmp"
            subprocess.call( cmd, shell=True)
            mvFlag=True
        cmd="touch "+flagFile
        subprocess.call( cmd, shell=True)
        # Success
        expected = True
        actual = self.target.checkFlag(flagFile)
        self.assertEqual(expected, actual)
        # Failed prepare
        cmd="rm -f "+flagFile
        subprocess.call( cmd, shell=True)
        #Failed
        expected = False
        actual = self.target.checkFlag(flagFile)
        self.assertEqual(expected, actual)
        if mvFlag:
            cmd = "mv /tmp/constantMagnification.flag " + flagFile
            subprocess.call(cmd, shell=True)

    def test_csv_write(self):
        # Failed prepare
        import subprocess
        cmd = "mkdir /tmp/flagdir_forunittest"
        subprocess.call(cmd, shell=True)
        # Failed
        expected = 1
        actual = util.csv_write("/tmp/flagdir_forunittest",[["aaa","aaaa","aaaaa"],["bbb","bbbb","bbbbb"]])
        self.assertEqual(expected, actual)
        cmd = "rm -rf /tmp/flagdir_forunittest"
        subprocess.call(cmd,shell=True)
        # Success
        expected = 0
        actual = util.csv_write("/tmp/flagdir_forunittest", [["aaa", "aaaa", "aaaaa"], ["bbb", "bbbb", "bbbbb"]])
        self.assertEqual(expected, actual)
        cmd = "rm -rf /tmp/flagdir_forunittest"
        subprocess.call(cmd,shell=True)

    def test_csv_read(self):
        # Failed
        expected = 1
        actual,data = util.csv_read("/tmp/flagdir_forunittest")
        self.assertEqual(expected, actual)
        # Success prepare
        util.csv_write("/tmp/flagdir_forunittest", [[111, 1111, 11111], [222, 2222, 22222]])
        # Success
        import subprocess
        expected = 0
        actual, data = util.csv_read("/tmp/flagdir_forunittest")
        self.assertEqual(expected, actual)
        self.assertEqual(data, [[111, 1111, 11111], [222, 2222, 22222]])
        cmd = "rm -rf /tmp/flagdir_forunittest"
        subprocess.call(cmd, shell=True)

    def test_remFile(self):
        # Failed prepare
        import subprocess
        cmd = "mkdir /tmp/flagdir_forunittest"
        subprocess.call(cmd, shell=True)
        # Failed
        expected = 1
        actual = util.remFile("/tmp/flagdir_forunittest")
        self.assertEqual(expected, actual)
        cmd = "rm -rf /tmp/flagdir_forunittest"
        subprocess.call(cmd,shell=True)
        # Success prepare
        cmd="touch /tmp/flagdir_forunittest"
        subprocess.call( cmd, shell=True)
        # Success
        expected = 0
        actual = util.remFile("/tmp/flagdir_forunittest")
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    # unittestを実行
    unittest.main()
