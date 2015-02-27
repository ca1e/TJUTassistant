# -*- coding: utf-8 -*-

import sys,os
from PIL import Image

im = Image.open('vecode.jpg')
w,h = im.size
xs = [0,17,34,49,w-3]
result = []
for i ,x in enumerate(xs):
	if(i+1>=len(xs)):
		break
	box = (x,0,xs[i+1],h)
	t = im.crop(box).copy()
	a = 'num_%d_%d_%d_%d'%box
	t.save(a+ '.jpg')
	