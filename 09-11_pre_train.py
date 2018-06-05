# -*- coding: utf-8 -*-
# @Time    : 2017/9/11 16:09
# @Author  : Lxy
# @Site    : 
# @File    : 09-11.py
# @Software: PyCharm
import csv
import re
#stu1 = ['marry', 26]
#stu2 = ['bob', 23]
#out = open('09-11.csv','a',newline='')
#csv_write = csv.writer(out, dialect='excel')

def findStr(string, subStr, findCnt):
    listStr = string.split(subStr,findCnt)
    if len(listStr) <= findCnt:
        return -1
    return len(string)-len(listStr[-1])-len(subStr)


#out = open('09-12.csv','a',newline='')
#csv_write = csv.writer(out, dialect='excel')
#zong_write = csv.writer(open('predict_37/0914-dev.csv','a',newline=''), dialect='excel')

dec_write = csv.writer(open('predict_37/DEC.csv','a',newline=''), dialect='excel')
nov_write = csv.writer(open('predict_37/NOV.csv','a',newline=''), dialect='excel')
jul_write = csv.writer(open('predict_37/JUL.csv','a',newline=''), dialect='excel')
aug_write = csv.writer(open('predict_37/AUG.csv','a',newline=''), dialect='excel')
sep_write = csv.writer(open('predict_37/SEP.csv','a',newline=''), dialect='excel')
oct_write = csv.writer(open('predict_37/OCT.csv','a',newline=''), dialect='excel')
#
###写入头信息#########
'''
PPPP = ['ID_string','dev','pyear_month','od_cnt','actual_od_cnt', 'virtual_od_cnt', 'od_brw', 'actual_od_brw', 'virtual_od_brw',
                   'cumu_od_cnt', 'cumu_actual_od_cnt', 'cumu_virtual_od_cnt', 'cumu_od_brw', 'cumu_actual_od_brw',
                   'cumu_virtual_od_brw', 'payed_capital', 'payed_mon_fee', 'payed_tot_fee', 'bal', 'paying_mon_fee',
                   'paying_tot_fee', 'foverdue_paying_day', 'foverdue_paying_cyc', 'foverdue_payed_day', 'foverdue_payed_cyc',
                   'fopen_to_buy']
PPPP = ['ID_string','dev','pyear_month','od_cnt','actual_od_cnt', 'virtual_od_cnt', 'od_zdfq_cnt', 'od_zdyq_cnt',
                   'od_brw', 'actual_od_brw', 'virtual_od_brw', 'od_zdfq_brw', 'od_zdyq_brw',
                   'cumu_od_cnt', 'cumu_actual_od_cnt', 'cumu_virtual_od_cnt','cumu_od_zdfq_cnt','cumu_od_zdyq_cnt',
                   'cumu_od_brw', 'cumu_actual_od_brw','cumu_virtual_od_brw', 'cumu_od_zdfq_brw', 'cumu_od_zdyq_brw',
                   'payed_capital', 'payed_mon_fee','payed_tot_fee', 'bal', 'zdfq_bal', 'zdyq_bal', 'paying_mon_fee',
                   'zdfq_paying_mon_fee', 'zdyq_paying_mon_fee','paying_tot_fee', 'zdfq_paying_tot_fee', 'zdyq_paying_tot_fee',
                   'foverdue_paying_day', 'foverdue_paying_cyc', 'foverdue_payed_day', 'foverdue_payed_cyc','fopen_to_buy']'''
#zong_write.writerow(PPPP)
'''
may_write.writerow(PPPP)
jun_write.writerow(PPPP)
jul_write.writerow(PPPP)
aug_write.writerow(PPPP)
sep_write.writerow(PPPP)
oct_write.writerow(PPPP)
'''
csv_file = csv.reader(open('lexin/test/val/ud_offtime.csv', 'r',encoding='utf-8'))
f = open('lexin/test/val/p6M_offtime.csv', 'r')

lines = f.readlines()
i_num = 0
#print(csv_file)
for ID in csv_file:
    SUM= "".join(ID)  #list转string
    ID_string = SUM[:32]
    #dev = SUM[32]
    dev=0
    i_num +=1
    print(i_num)

    #print(ID_string[:32])
    for line in lines:
        #m = re.match(ID_string, line)
        #print(line)
        if  ID_string in line:
            #print(ID_string)
            #iii +=1
            #print(line)

            pyear_month =       line[findStr(line, ',', 1)  + 1:findStr(line, ',', 2)]
            od_cnt =            line[findStr(line, ',', 3)  + 1:findStr(line, ',', 4)]
            actual_od_cnt =     line[findStr(line, ',', 4)  + 1:findStr(line, ',', 5)]
            virtual_od_cnt =    line[findStr(line, ',', 5)  + 1:findStr(line, ',', 6)]
            od_zdfq_cnt =       line[findStr(line, ',', 11) + 1:findStr(line, ',', 12)]
            od_zdyq_cnt =       line[findStr(line, ',', 13) + 1:findStr(line, ',', 14)]
            od_brw =            line[findStr(line, ',', 15) + 1:findStr(line, ',', 16)]
            actual_od_brw =     line[findStr(line, ',', 16) + 1:findStr(line, ',', 17)]
            virtual_od_brw =    line[findStr(line, ',', 17) + 1:findStr(line, ',', 18)]
            od_zdfq_brw =       line[findStr(line, ',', 23) + 1:findStr(line, ',', 24)]
            od_zdyq_brw =       line[findStr(line, ',', 25) + 1:findStr(line, ',', 26)]
            cumu_od_cnt =       line[findStr(line, ',', 27) + 1:findStr(line, ',', 28)]
            cumu_actual_od_cnt= line[findStr(line, ',', 28) + 1:findStr(line, ',', 29)]
            cumu_virtual_od_cnt=line[findStr(line, ',', 29) + 1:findStr(line, ',', 30)]
            cumu_od_zdfq_cnt=   line[findStr(line, ',', 35) + 1:findStr(line, ',', 36)]
            cumu_od_zdyq_cnt=   line[findStr(line, ',', 37) + 1:findStr(line, ',', 38)]
            cumu_od_brw =       line[findStr(line, ',', 39) + 1:findStr(line, ',', 40)]
            cumu_actual_od_brw= line[findStr(line, ',', 40) + 1:findStr(line, ',', 41)]
            cumu_virtual_od_brw=line[findStr(line, ',', 41) + 1:findStr(line, ',', 42)]
            cumu_od_zdfq_brw=   line[findStr(line, ',', 47) + 1:findStr(line, ',', 48)]
            cumu_od_zdyq_brw=   line[findStr(line, ',', 49) + 1:findStr(line, ',', 50)]
            payed_capital =     line[findStr(line, ',', 51) + 1:findStr(line, ',', 52)]
            payed_mon_fee =     line[findStr(line, ',', 63) + 1:findStr(line, ',', 64)]
            payed_tot_fee =     line[findStr(line, ',', 73) + 1:findStr(line, ',', 74)]
            bal =               line[findStr(line, ',', 83) + 1:findStr(line, ',', 84)]
            zdfq_bal=           line[findStr(line, ',', 89) + 1:findStr(line, ',', 90)]
            zdyq_bal=           line[findStr(line, ',', 91) + 1:findStr(line, ',', 92)]
            paying_mon_fee =    line[findStr(line, ',', 93) + 1:findStr(line, ',', 94)]
            zdfq_paying_mon_fee=line[findStr(line, ',', 99) + 1:findStr(line, ',', 100)]
            zdyq_paying_mon_fee=line[findStr(line, ',', 101)+ 1:findStr(line, ',', 102)]
            paying_tot_fee =    line[findStr(line, ',', 103)+ 1:findStr(line, ',', 104)]
            zdfq_paying_tot_fee=line[findStr(line, ',', 109)+ 1:findStr(line, ',', 110)]
            zdyq_paying_tot_fee=line[findStr(line, ',', 111)+ 1:findStr(line, ',', 112)]
            foverdue_paying_day=line[findStr(line, ',', 121)+ 1:findStr(line, ',', 122)]
            foverdue_paying_cyc=line[findStr(line, ',', 122)+ 1:findStr(line, ',', 123)]
            foverdue_payed_day= line[findStr(line, ',', 123)+ 1:findStr(line, ',', 124)]
            foverdue_payed_cyc= line[findStr(line, ',', 124)+ 1:findStr(line, ',', 125)]
            fopen_to_buy =      line[findStr(line, ',', 129)+ 1:findStr(line, ',', 130)]
            #print(ID_string)
            #print(x_3_4)
            mmm = [ID_string,dev,pyear_month,od_cnt,actual_od_cnt, virtual_od_cnt, od_zdfq_cnt, od_zdyq_cnt,
                   od_brw, actual_od_brw, virtual_od_brw, od_zdfq_brw, od_zdyq_brw,
                   cumu_od_cnt, cumu_actual_od_cnt, cumu_virtual_od_cnt,cumu_od_zdfq_cnt,cumu_od_zdyq_cnt,
                   cumu_od_brw, cumu_actual_od_brw,cumu_virtual_od_brw, cumu_od_zdfq_brw, cumu_od_zdyq_brw,
                   payed_capital, payed_mon_fee,payed_tot_fee, bal, zdfq_bal, zdyq_bal, paying_mon_fee,
                   zdfq_paying_mon_fee, zdyq_paying_mon_fee,paying_tot_fee, zdfq_paying_tot_fee, zdyq_paying_tot_fee,
                   foverdue_paying_day, foverdue_paying_cyc, foverdue_payed_day, foverdue_payed_cyc,fopen_to_buy]
            #zong_write.writerow(mmm)
            #csv_write.writerow(mmm )

            if pyear_month[2:5] == 'DEC':
                #print('DEC')
                dec_write.writerow(mmm)
            elif pyear_month[2:5] == 'NOV':
                #print('NOV')
                nov_write.writerow(mmm)
            elif pyear_month[2:5] == 'JUL':
                #print('JUL')
                jul_write.writerow(mmm)
            elif pyear_month[2:5] == 'AUG':
                #print('AUG')
                aug_write.writerow(mmm)
            elif pyear_month[2:5] == 'SEP':
                #print('SEP')
                sep_write.writerow(mmm)
            elif pyear_month[2:5] == 'OCT':
                #print('OCT')
                oct_write.writerow(mmm)


    #csv_write.writerow(x,)'''
