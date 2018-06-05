import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.cross_validation import train_test_split
import time

time_start = time.time()
ID = 'ID_string'
target = 'dev'
data = 'pyear_month'
money = 'actual_od_brw_f6m'
train = pd.read_csv('0919-zong.csv')
#x_columns = [x for x in train.columns if x not in [ID,  data,'cyc_date', 'fcredit_update_time',target, money]]
x_columns = [x for x in ['futilization', 'fopen_to_buy', 'credit_limit', 'foverdue_payed_cyc', 'foverdue_payed_day',
                         'foverdue_paying_cyc', 'foverdue_paying_day', 'acre_repay_od_cpt', 'payed_comp_act_od_cnt',
                         'zdfq_paying_tot_fee', 'xj_paying_tot_fee', 'paying_tot_fee', 'zdfq_paying_mon_fee',
                         'xj_paying_mon_fee', 'yl_paying_mon_fee', 'paying_mon_fee', 'ptsh_bal', 'xj_bal', 'yl_bal',
                         'bal', 'payed_ptsh_tot_fee', 'payed_xj_tot_fee', 'payed_yl_tot_fee', 'payed_3c_tot_fee',
                         'payed_xj_mon_fee', 'payed_3c_capital', 'payed_actual_capital', 'cumu_od_zdfq_brw',
                         'cumu_od_xj_brw', 'cumu_od_yl_brw', 'cumu_od_3c_brw', 'cumu_actual_od_brw', 'cumu_virtual_od_cnt']]
y = train[target]
#z = train[money]
X = train[x_columns]

#print(train.head(0))

X_train_t, X_test_t, y_train, y_test = train_test_split(X, y, test_size=0.5)
############参数寻优




grd = GradientBoostingClassifier(learning_rate=0.01, n_estimators=1800,max_depth=2, min_samples_split= 700,
                                                               min_samples_leaf= 60,max_features=2,
                                                             subsample=0.8, random_state=10)
grd = GradientBoostingClassifier(random_state=10)
grd.fit(X_train_t, y_train)
y_pred_grd = grd.predict_proba(X_test_t)[:, 1]
roc_auc = metrics.roc_auc_score(y_test, y_pred_grd)
print('DEV predict:', roc_auc)
feature = grd.feature_importances_

#print(feature)
print(feature.shape)
'''
X_train_m, X_test_m, z_train, z_test = train_test_split(X, z, test_size=0.5)
grl = GradientBoostingRegressor(random_state=10)
grl.fit(X_train_t, z_train)
z_pred_frl = grl.score(X_test_m, z_test)
print('回归得分：', z_pred_frl)
print(grl.feature_importances_)
print(grl.feature_importances_.shape)
'''
time_end = time.time()
print('运行时间：', time_end-time_start, 's')
'''
t = 0
num = 0
for f in feature:
    num +=1
    if f>0.01:
        t += 1
        print('特征强度：',f, '     第%d位：'%num)

print("现在特征数是：", t)'''