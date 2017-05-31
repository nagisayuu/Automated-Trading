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
		self.target = Algorithm.AlgExecutor("XETHZJPY",os.path.dirname(os.path.abspath(__file__))+"/../../../key/kraken.key.dum")
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../src/')
	# テストメソッドの実行が終わるたびに呼ばれる
	def tearDown(self):
		if sys.flags.debug: print(os.linesep + '> tearDown method is called.')
		sys.path.remove(os.path.dirname(os.path.abspath(__file__)) + '/../../../src/')
		# setUpで準備したオブジェクトを解放する
		del(self.target)

	def test_setFile(self):
		expected = 'hoge'
		self.target.setFile('hoge')
		self.assertEqual(expected, self.target.filename)

	def test_setMagnification(self):
		expected = 'hoge'
		self.target.setMagnification('hoge')
		self.assertEqual(expected, self.target.magnification)

	def test_fetchPrice(self):
		expectedFlag = True
		actualFlag,actualData = self.target.fetchPrice()
		self.assertEqual(expectedFlag, actualFlag)

	def test_checkFlag(self):
		# Success prepare
		import subprocess
		mvFlag = False
		curdir=os.path.dirname(os.path.abspath(__file__))
		flagFile = os.path.join(curdir, '../../../flag/constantMagnification.flag')
		if os.path.isfile(flagFile):
			cmd="/bin/mv "+flagFile+" /tmp"
			subprocess.call( cmd, shell=True)
			mvFlag=True
		cmd="/bin/touch "+flagFile
		subprocess.call( cmd, shell=True)
		# Success
		expectedFlag = True
		actualFlag = self.target.checkFlag()
		self.assertEqual(expectedFlag, actualFlag)
		# Failed prepare
		cmd="/bin/rm -f "+flagFile
		subprocess.call( cmd, shell=True)
		#Failed
		expectedFlag = False
		actualFlag = self.target.checkFlag()
		self.assertEqual(expectedFlag, actualFlag)
		if mvFlag:
			cmd="/bin/mv /tmp/constantMagnification.flag "+flagFile
			subprocess.call( cmd, shell=True	)

	def test_execute(self):
		# Buy prepare
		import subprocess
		mvFlag = False
		curdir=os.path.dirname(os.path.abspath(__file__))
		flagFile = os.path.join(curdir, '../../../flag/constantMagnification.flag')
		if os.path.isfile(flagFile):
			cmd="/bin/mv "+flagFile+" /tmp"
			subprocess.call( cmd, shell=True)
			mvFlag=True
		# Buy
		expectedOperate = "buy"
		actualOperate = self.target.execute()[0]
		self.assertEqual(expectedOperate, actualOperate)

		# Sell prepare
		cmd="/bin/echo '0,0,0' >"+flagFile
		subprocess.call( cmd, shell=True)

		# Sell
		expectedOperate = "sell"
		actualOperate = self.target.execute()[0]
		self.assertEqual(expectedOperate, actualOperate)

		# Wait prepare
		cmd="/bin/echo '999999999999999,999999999999999,999999999999999' >"+flagFile
		subprocess.call( cmd, shell=True)

		# Wait
		expectedOperate = "wait"
		actualOperate = self.target.execute()[0]
		self.assertEqual(expectedOperate, actualOperate)

		cmd="/bin/rm -f "+flagFile
		subprocess.call( cmd, shell=True)

		if mvFlag:
			cmd="/bin/mv /tmp/constantMagnification.flag "+flagFile
			subprocess.call(cmd, shell=True)

if __name__ == '__main__':
	# unittestを実行
	unittest.main()
