# -*- coding: utf-8 -*-

import random
import sys
import time
import socket
from PIL import Image
import urllib.request, urllib.parse, urllib.error

socket.setdefaulttimeout(5) 
err = []
okk = []
def Randurl():
    veurl = r'http://ssfw.tjut.edu.cn/ssfw/jwcaptcha.do?'
    return veurl + str(random.randint(1,100))

def Identification(filepath):
    threshold = 196
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    im = Image.open(filepath)
    imgry = im.convert('L')
    out = imgry.point(table,'1')
    #out = im.convert('1')
    out.save(filepath)

def getvecode(i):
    filepath = 'vecode'+ str(i) + '.jpg'
    try:
    	v = urllib.request.urlopen(Randurl()).read()
    except Exception as e:
    	err.append(i)
    	print(str(i) + '-----Failed')
    else:
        f = open(filepath,'wb')
        f.write(v)
        f.close()
        Identification(filepath)
        okk.append(i)
        print(str(i) + '--OK')

for i in range(100):
	getvecode(i)
print(err)
while len(err)>0:
    for i in err:
    	getvecode(i)
    err = [i for i in err if not i in okk]