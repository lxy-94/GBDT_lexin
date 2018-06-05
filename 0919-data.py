import time
import progressbar
import csv

PPPP = ['ID_string', 'pyear_month', 'cyc_date', 'od_cnt', 'actual_od_cnt', 'virtual_od_cnt', 'od_3c_cnt', 'od_bh_cnt', 'od_yl_cnt', 'od_xj_cnt', 'od_ptsh_cnt', 'od_zdfq_cnt', 'od_xssh_cnt', 'od_zdyq_cnt',
     'od_lh_new_cnt', 'od_brw', 'actual_od_brw', 'virtual_od_brw', 'od_3c_brw', 'od_bh_brw', 'od_yl_brw',
     'od_xj_brw', 'od_ptsh_brw', 'od_zdfq_brw', 'od_xssh_brw', 'od_zdyq_brw', 'od_lh_new_brw', 'cumu_od_cnt', 'cumu_actual_od_cnt', 'cumu_virtual_od_cnt', 'cumu_od_3c_cnt',
     'cumu_od_bh_cnt', 'cumu_od_yl_cnt', 'cumu_od_xj_cnt', 'cumu_od_ptsh_cnt', 'cumu_od_zdfq_cnt', 'cumu_od_xssh_cnt', 'cumu_od_zdyq_cnt', 'cumu_od_lh_new_cnt', 'cumu_od_brw', 'cumu_actual_od_brw', 'cumu_virtual_od_brw',
     'cumu_od_3c_brw', 'cumu_od_bh_brw', 'cumu_od_yl_brw', 'cumu_od_xj_brw', 'cumu_od_ptsh_brw', 'cumu_od_zdfq_brw', 'cumu_od_xssh_brw', 'cumu_od_zdyq_brw', 'cumu_od_lh_new_brw', 'payed_capital', 'payed_actual_capital', 'payed_virtual_capital', 'payed_3c_capital', 'payed_bh_capital', 'payed_yl_capital', 'payed_xj_capital', 'payed_ptsh_capital', 'payed_zdfq_capital',
     'payed_xssh_capital', 'payed_zdyq_capital', 'payed_lh_new_capital', 'payed_mon_fee', 'payed_3c_mon_fee', 'payed_bh_mon_fee', 'payed_yl_mon_fee', 'payed_xj_mon_fee',
     'payed_ptsh_mon_fee', 'payed_zdfq_mon_fee', 'payed_xssh_mon_fee', 'payed_zdyq_mon_fee', 'payed_lh_new_mon_fee', 'payed_tot_fee', 'payed_3c_tot_fee', 'payed_bh_tot_fee', 'payed_yl_tot_fee', 'payed_xj_tot_fee', 'payed_ptsh_tot_fee', 'payed_zdfq_tot_fee', 'payed_xssh_tot_fee', 'payed_zdyq_tot_fee', 'payed_lh_new_tot_fee', 'bal', 'ds3c_bal', 'bh_bal', 'yl_bal',
     'xj_bal', 'ptsh_bal', 'zdfq_bal', 'xssh_bal', 'zdyq_bal', 'lh_new_bal', 'paying_mon_fee', 'ds3c_paying_mon_fee', 'bh_paying_mon_fee',
     'yl_paying_mon_fee', 'xj_paying_mon_fee', 'ptsh_paying_mon_fee', 'zdfq_paying_mon_fee', 'xssh_paying_mon_fee', 'zdyq_paying_mon_fee', 'lh_new_paying_mon_fee', 'paying_tot_fee', 'ds3c_paying_tot_fee',
     'bh_paying_tot_fee', 'yl_paying_tot_fee', 'xj_paying_tot_fee', 'ptsh_paying_tot_fee', 'zdfq_paying_tot_fee', 'xssh_paying_tot_fee', 'zdyq_paying_tot_fee', 'lh_new_paying_tot_fee', 'paying_complete_od_cnt', 'payed_complete_od_cnt', 'payed_comp_act_od_cnt', 'paying_complete_od_brw', 'payed_complete_od_brw', 'payed_comp_act_od_brw', 'acre_repay_od_cnt',
     'acre_repay_od_cpt', 'foverdue_paying_day', 'foverdue_paying_cyc', 'foverdue_payed_day', 'foverdue_payed_cyc', 'cpt_pymt', 'credit_limit', 'fcredit_update_time', 'futilization', 'fopen_to_buy', 'dev', 'actual_od_brw_f6m']

zong_write = csv.writer(open('zong.csv','a',newline=''), dialect='excel')
zong_write.writerow(PPPP)

def findStr(string, subStr, findCnt):
    listStr = string.split(subStr,findCnt)
    if len(listStr) <= findCnt:
        return -1
    return len(string)-len(listStr[-1])-len(subStr)

csv___cc = open('C:/Users\lxy\Documents\GitHub\机器学习代码\GBDT\dep_mdl.csv','r')
next(csv___cc)
csv_file = csv___cc.readlines()
f = open('C:/Users\lxy\Documents\GitHub\机器学习代码\GBDT/6geyue.csv', 'r')
next(f)
lines = f.readlines()
i_num = 0
N = 50000
p = progressbar.ProgressBar()
p.start(N)

for ID in csv_file:
    time.sleep(0.01)
    p.update(i_num+1)
    i_num +=1
    actual_od_brw_f6m = ID[findStr(ID, ',', 2) + 1:findStr(ID, ',', 3)]
    ID_string = ID[:findStr(ID, ',', 1)]
    dev = ID[findStr(ID, ',', 1) + 1:findStr(ID, ',', 2)]
    for line in lines:
        if  ID_string in line:
            mmmm = [line[findStr(line, ',', m) + 1:findStr(line, ',', m + 1)] for m in range(130)]
            mmmm.append(dev)
            mmmm.append(actual_od_brw_f6m)
            zong_write.writerow(mmmm)


