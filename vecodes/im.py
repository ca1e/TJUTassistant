
import sys,os
#import numpy
from PIL import Image
#im = Image.open('4.jpg')
im1 = Image.open('5.jpg')
#a = im.histogram()
b = im1.histogram()
box=(1,0,17,22)
imr = im1.crop(box)
imr.save('1.jpg')
# def split_image(img, part_size = (64, 64)):
# 	w, h = img.size
# 	pw, ph = part_size
# 	assert w % pw == h % ph == 0
# 	return [img.crop((i, j, i+pw, j+ph)).copy() for i in range(0, w, pw) for j in range(0, h, ph)]

# def hist_similar(lh, rh):
# 	assert len(lh) == len(rh)
# 	return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)
    
# def calc_similar(li, ri):
# 	return hist_similar(li.histogram(), ri.histogram())
# 	#return sum(hist_similar(l.histogram(), r.histogram()) for l, r in zip(split_image(li), split_image(ri))) / 16.0


#print(calc_similar(im,im1)*100)
#print(len(a))
# print(len(b))
# N = len(a)

# narr = numpy.array(a)
# sum1 = narr.sum()
# narr2 = narr*narr
# sum2 = narr2.sum()
# mean = sum1/N
# var=sum2/N-mean**2
# print(sum1,sum2,var)