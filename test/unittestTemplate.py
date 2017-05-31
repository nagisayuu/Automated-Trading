#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os,re,unittest
# 対象ファイルをパスに追加
rootDir=re.sub(r'/test/.*','',os.path.dirname(os.path.abspath(__file__)))
targetFile=rootDir+'/src'+re.sub(rootDir+'/test','',os.path.dirname(os.path.abspath(__file__)))+'.py'
targetDir=os.path.dirname(targetFile)

sys.path.append(targetDir)

import constantMagnification as Algorithm
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
		self.target = Algorithm.AlgExecutor.()

	# テストメソッドの実行が終わるたびに呼ばれる
	def tearDown(self):
		if sys.flags.debug: print(os.linesep + '> tearDown method is called.')
		# setUpで準備したオブジェクトを解放する
		del(self.target)

	def test_hoge(self):
		expected = 'hoge'
		actual = self.smpl.return_hoge()
		self.assertEqual(expected, actual)

	def test_poyo(self):
		expected = 'poyo'
		actual = self.smpl.return_hoge() # 凡ミス
		self.assertEqual(expected, actual)

if __name__ == '__main__':
	# unittestを実行
	unittest.main()
