# -*- coding: utf-8 -*-

from imgprocess import *

#vecode_to_string()
def getfilepath(n):
	s = '1\\vecode'+ str(n) +'.jpg'
	return s
con = 0
for i in range(100):
	s = getfilepath(i)
	r = vecode_to_string(s)
	if(r=='null'):
		con = con + 1
print(con/100)