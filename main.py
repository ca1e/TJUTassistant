# -*- coding: utf-8 -*-

import tjutlogn,imgprocess
import sys,os
import tempfile
#from PyQt4 import QtCore,QtGui

def main(user,pwd,option,info):
    m = tjutlogn.Tjut()
    rl = ''
    tmpfd, tempfilename = tempfile.mkstemp()
    vepath = tempfilename + '.jpg'
    cont = 0
    while not rl=='success':
        while True:
            cont = cont + 1
            v = m.getvecode(vepath)
            if v:break
            if op == '-v' :
                print("Access Verificode failed, try again..")
        imgprocess.Identification(vepath)
        #识别验证码
        verify = imgprocess.vecode_to_string(vepath)
        #登陆
        rl = m.Login(user,pwd,verify)
        if rl=='validateCodeError':
            if op == '-v' :
                print('Identify the vecode error,try again..')
            continue
        elif rl=='userNameOrPasswordError':
            print('学号或密码错误')
            return False
    name = m.GetName()
    num = m.GetNum()
    m.PostYourPasswd(user,pwd)
    print('登陆成功！以下为显示信息:')
    print("姓名:",name)
    print("学号:",num)
    #m.DownFace()
    if info=='titable':
        m.GetTimetable()
    elif info=='record':
        m.GetMyRecord("2014-2015",'1')
    return True
            

def help():
    print('[options]:')
    print('-h:  显示此信息')
    print('-v:  显示登陆的详细信息')
    print('[info]:')
    print('titable:  保存课表')
    print('record :  保存成绩')


user = ''
pwd = ''
op = ''
info = ''
ops = ['-h','-v']
infos = ['titable',
        'record']

if __name__=='__main__':
    if len(sys.argv)<3:
        print('usage:',sys.argv[0],'[options] usrname password [info]')
        help()
    else:
        user = sys.argv[1]
        pwd = sys.argv[2]
        if len(sys.argv)>=4:
            if sys.argv[1] in ops:
                op = sys.argv[1]
                user = sys.argv[2]
                pwd = sys.argv[3]
                if len(sys.argv)==5:
                    info = sys.argv[4]
            else:
                if sys.argv[3] in infos:
                    info = sys.argv[3]
                else:
                    print('infos put error:',info)
        main(user,pwd,op,info)
