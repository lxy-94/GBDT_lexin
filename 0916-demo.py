# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 14:45
# @Author  : Lxy
# @Site    : 
# @File    : lexin_demo.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.cross_validation import train_test_split
import matplotlib.pylab as plt

ID = 'ID_string'
target = 'dev'
data = 'pyear_month'
#f_result=open('OCT_9.txt', 'w')
train = pd.read_csv('OCT.csv')
x_columns = [x for x in train.columns if x not in ['ID_string','dev','pyear_month','od_cnt','actual_od_cnt', 'virtual_od_cnt', 'od_brw', 'actual_od_brw',
                   'cumu_od_cnt', 'cumu_actual_od_cnt', 'cumu_virtual_od_cnt', 'cumu_od_brw', 'cumu_actual_od_brw',
                    'payed_capital', 'payed_mon_fee', 'payed_tot_fee', 'bal',
                    'foverdue_paying_day', 'foverdue_paying_cyc', 'foverdue_payed_cyc']]
y = train['dev']
X = train[x_columns]
#print(train['dev'].value_counts())
'''
Test_1 = pd.read_csv('predict/OCT.csv')
x_test_1 = [x for x in Test_1.columns if x not in [ID, target, data]]

X_test_1 = Test_1[x_test_1]
'''


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

#print(len(X_train), len(X_test), len(y_train), len(y_test))
X_train, X_train_lr, y_train, y_train_lr = train_test_split(X_train, y_train, test_size=0.5)
#print(len(X_train), len(X_train_lr), len(y_train), len(y_train_lr))

#grd = GradientBoostingClassifier(n_estimators=n_estimator)
grd = GradientBoostingClassifier(learning_rate=0.01, n_estimators=800,max_depth=2, min_samples_split= 700,
                                                               min_samples_leaf= 60,max_features=2,
                                                             subsample=0.8, random_state=10)
grd_enc = OneHotEncoder()
grd_lm = LogisticRegression()
grd.fit(X_train,y_train)
y_pred_grd = grd.predict_proba(X_test)[:, 1]

fpr_grd, tpr_grd, _ = metrics.roc_curve(y_test, y_pred_grd)
roc_auc = metrics.roc_auc_score(y_test, y_pred_grd)
print('predict:', roc_auc)
grd_enc.fit(grd.apply(X_train)[:, :, 0])
grd_lm.fit(grd_enc.transform(grd.apply(X_train_lr)[:, :, 0]), y_train_lr)
y_pred_grd_lm = grd_lm.predict_proba(grd_enc.transform(grd.apply(X_test)[:, :, 0]))[:, 1]
#fpr_grd_lm, tpr_grd_lm, _ = metrics.roc_curve(y_test, y_pred_grd_lm)
roc_auc = metrics.roc_auc_score(y_test, y_pred_grd_lm)
print('predict:',roc_auc)
#print('AUC Score', (metrics.roc_curve(y_test, y_pred_grd_lm)))
#print(y_pred_grd_lm )





gbm0 = GradientBoostingClassifier(learning_rate=0.01, n_estimators=800,max_depth=21,max_features=2,min_samples_split= 700,
                                                               min_samples_leaf= 60,
                                                             subsample=0.8, random_state=10)
gbm0.fit(X_train, y_train)
#y_pred = gbm0.predict(X)
y_predprod = gbm0.predict_proba(X_test)[:,1]
print('AUC Score (Train): %f' % metrics.roc_auc_score(y_test, y_predprod) )
'''

#m_s_s:700:0.909
param_test1 = { 'max_features': list(range(1,5,1))}
gsearch1 = GridSearchCV(estimator=GradientBoostingClassifier(learning_rate=0.1, n_estimators=80,max_depth=21, min_samples_split= 700,
                                                               min_samples_leaf= 60,
                                                             subsample=0.8, random_state=10)
                        , param_grid=param_test1, scoring='roc_auc',iid=False,cv=5)
gsearch1.fit(X_train, y_train)
print(gsearch1.best_params_, gsearch1.best_score_)

for i in range(50000):
    y_auc = round(y_pred_grd[i], 4)
    print(Test_1[ID][i], y_auc, i)

    f_result.write(Test_1[ID][i])
    f_result.write(' ')
    f_result.write(str(y_auc))
    f_result.write('\n')
f_result.close()
    #f_result.write(Test[ID][i])

#print(y_pred)
#print(y_predprod)
#print('Accuracy: %.4g' % metrics.accuracy_score(y.values, y_pred))
#print('AUC Score (Train): %f' % metrics.roc_auc_score(y, y_predprod) )'''

