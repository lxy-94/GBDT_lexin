# -*- coding: utf-8 -*-
# @Time    : 2017/10/29 15:34
# @Author  : Lxy
# @Site    : 
# @File    : 1029.py
# @Software: PyCharm
import csv

pppp = ['ID', 'ret']
num = 1

zong_write = csv.writer(open(str(num)+'.csv','a',newline=''), dialect='excel')
zong_write.writerow(pppp)
f = open("1029.txt","r")
lines = f.readlines()#读取全部内容
for line in lines:
    line = line.strip('\n')
    mmmm=[num,line]
    print(line)
    zong_write.writerow(mmmm)
f.close()

