
# @Time    : 2017/9/12 15:21
# @Author  : Lxy
# @Site    : 
# @File    : pre_test.py
# @Software: PyCharm

import csv
import re
import time
import progressbar
p = progressbar.ProgressBar()
def findStr(string, subStr, findCnt):
    listStr = string.split(subStr,findCnt)
    if len(listStr) <= findCnt:
        return -1
    return len(string)-len(listStr[-1])-len(subStr)
PPPP = ['ID_string','dev', 'actual_od_brw_f6m','pyear_month','od_cnt','actual_od_cnt', 'virtual_od_cnt', 'od_brw', 'actual_od_brw', 'virtual_od_brw',
                   'cumu_od_cnt', 'cumu_actual_od_cnt', 'cumu_virtual_od_cnt', 'cumu_od_brw', 'cumu_actual_od_brw',
                   'cumu_virtual_od_brw', 'payed_capital', 'payed_mon_fee', 'payed_tot_fee', 'bal', 'paying_mon_fee',
                   'paying_tot_fee', 'foverdue_paying_day', 'foverdue_paying_cyc', 'foverdue_payed_day', 'foverdue_payed_cyc',
                   'fopen_to_buy']

#out = open('09-19.csv','a',newline='')
#csv_write = csv.writer(out, dialect='excel')
#zong_write = csv.writer(open('predict/zong.csv','a',newline=''), dialect='excel')
'''
may_write = csv.writer(open('predict/MAY.csv','a',newline=''), dialect='excel')
jun_write = csv.writer(open('predict/JUN.csv','a',newline=''), dialect='excel')
jul_write = csv.writer(open('predict/JUL.csv','a',newline=''), dialect='excel')
aug_write = csv.writer(open('predict/AUG.csv','a',newline=''), dialect='excel')
sep_write = csv.writer(open('predict/SEP.csv','a',newline=''), dialect='excel')
oct_write = csv.writer(open('predict/OCT.csv','a',newline=''), dialect='excel')
#
###写入头信息#########



may_write.writerow(PPPP)
jun_write.writerow(PPPP)
jul_write.writerow(PPPP)
aug_write.writerow(PPPP)
sep_write.writerow(PPPP)
oct_write.writerow(PPPP)'''
#csv_write.writerow(PPPP)

#csv_file = csv.reader(open('lexin/train/dep_mdl.csv', 'r', encoding='UTF-8'))
csv___cc = open('dep_mdl.csv','r')
next(csv___cc)
csv_file = csv___cc.readlines()
f = open('6geyue.csv', 'r')

lines = f.readlines()
i_num = 0
N = 50000
p.start(N)
#print(csv_file)

for ID in csv_file:
    time.sleep(0.01)
    p.update(i_num+1)
    i_num +=1
    actual_od_brw_f6m = ID[findStr(ID, ',', 2) + 1:findStr(ID, ',', 3)]
    #SUM= "".join(ID)  #list转string
    #ID_string = SUM[:32]
    #actual_od_brw_f6m = 0
    ID_string = ID[:findStr(ID, ',', 1)]
    #dev = SUM[32]
    dev = ID[findStr(ID, ',', 1) + 1:findStr(ID, ',', 2)]
    #dev = 1
    #print( ID_string)
    #print(dev)
    #print(actual_od_brw_f6m)
    #dev = 0

    iii = 0
    #print(ID_string[:32])
    for line in lines:
        #m = re.match(ID_string, line)
        #print(line)
        if  ID_string in line:

            pyear_month =       line[findStr(line, ',', 1)  + 1:findStr(line, ',', 2)]
            od_cnt =            line[findStr(line, ',', 3)  + 1:findStr(line, ',', 4)]
            actual_od_cnt =     line[findStr(line, ',', 4)  + 1:findStr(line, ',', 5)]
            virtual_od_cnt =    line[findStr(line, ',', 5)  + 1:findStr(line, ',', 6)]
            od_brw =            line[findStr(line, ',', 15) + 1:findStr(line, ',', 16)]
            actual_od_brw =     line[findStr(line, ',', 16) + 1:findStr(line, ',', 17)]
            virtual_od_brw =    line[findStr(line, ',', 17) + 1:findStr(line, ',', 18)]
            cumu_od_cnt =       line[findStr(line, ',', 27) + 1:findStr(line, ',', 28)]
            cumu_actual_od_cnt= line[findStr(line, ',', 28) + 1:findStr(line, ',', 29)]
            cumu_virtual_od_cnt=line[findStr(line, ',', 29) + 1:findStr(line, ',', 30)]
            cumu_od_brw =       line[findStr(line, ',', 39) + 1:findStr(line, ',', 40)]
            cumu_actual_od_brw= line[findStr(line, ',', 40) + 1:findStr(line, ',', 41)]
            cumu_virtual_od_brw=line[findStr(line, ',', 41) + 1:findStr(line, ',', 42)]
            payed_capital =     line[findStr(line, ',', 51) + 1:findStr(line, ',', 52)]
            payed_mon_fee =     line[findStr(line, ',', 63) + 1:findStr(line, ',', 64)]
            payed_tot_fee =     line[findStr(line, ',', 73) + 1:findStr(line, ',', 74)]
            bal =               line[findStr(line, ',', 83) + 1:findStr(line, ',', 84)]
            paying_mon_fee =    line[findStr(line, ',', 93) + 1:findStr(line, ',', 94)]
            paying_tot_fee =    line[findStr(line, ',', 103)+ 1:findStr(line, ',', 104)]
            foverdue_paying_day=line[findStr(line, ',', 121)+ 1:findStr(line, ',', 122)]
            foverdue_paying_cyc=line[findStr(line, ',', 122)+ 1:findStr(line, ',', 123)]
            foverdue_payed_day= line[findStr(line, ',', 123)+ 1:findStr(line, ',', 124)]
            foverdue_payed_cyc= line[findStr(line, ',', 124)+ 1:findStr(line, ',', 125)]
            fopen_to_buy =      line[findStr(line, ',', 129)+ 1:findStr(line, ',', 130)]
            #print(ID_string)
            #print(x_3_4)
            mmm = [ID_string,dev,actual_od_brw_f6m,pyear_month,od_cnt,actual_od_cnt, virtual_od_cnt, od_brw, actual_od_brw, virtual_od_brw,
                   cumu_od_cnt, cumu_actual_od_cnt, cumu_virtual_od_cnt, cumu_od_brw, cumu_actual_od_brw,
                   cumu_virtual_od_brw, payed_capital, payed_mon_fee, payed_tot_fee, bal, paying_mon_fee,
                   paying_tot_fee, foverdue_paying_day, foverdue_paying_cyc, foverdue_payed_day, foverdue_payed_cyc,
                   fopen_to_buy]
            print(mmm)
            #csv_write.writerow(mmm )
            '''
            if pyear_month[2:5] == 'MAY':
                print('MAY')
                may_write.writerow(mmm)
            elif pyear_month[2:5] == 'JUN':
                print('JUN')
                jun_write.writerow(mmm)
            elif pyear_month[2:5] == 'JUL':
                print('JUL')
                jul_write.writerow(mmm)
            elif pyear_month[2:5] == 'AUG':
                print('AUG')
                aug_write.writerow(mmm)
            elif pyear_month[2:5] == 'SEP':
                print('SEP')
                sep_write.writerow(mmm)
            elif pyear_month[2:5] == 'OCT':
                print('OCT')
                oct_write.writerow(mmm)
    #csv_write.writerow(x,)'''
