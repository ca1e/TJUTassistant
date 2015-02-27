# -*- coding: utf-8 -*-

import os
from PIL import Image

def vecode_to_string(filepath):#识别验证码，准确率不高
    pipe=os.popen('ve.exe ' + filepath)
    verify = pipe.read().strip()
    return verify if len(verify)==4 else 'null'

def Identification(filepath):#处理验证码，无用
		threshold = 160
		table = []
		for i in range(256):
			if i < threshold:
				table.append(0)
			else:
				table.append(1)
		im = Image.open(filepath)
		im = im.convert('L')
		out = im.point(table,'1')
		out.save(filepath)