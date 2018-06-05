# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 14:45
# @Author  : Lxy
# @Site    : 
# @File    : lexin_demo.py
# @Software: PyCharm

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV
import matplotlib.pylab as plt
ID = 'ID_string'
target = 'dev'
data = 'pyear_month'

train = pd.read_csv('0913-zong.csv')
x_columns = [x for x in train.columns if x not in [ID, target, data]]
X = train[x_columns]
y = train['dev']

Test = pd.read_csv('predict/OCT.csv')
x_test = [x for x in Test.columns if x not in [ID, target, data]]
X_test = Test[x_test]
'''
Test_sep = pd.read_csv('predict/SEP.csv')
x_test_sep = [x for x in Test.columns if x not in [ID, target, data]]
X_test_sep = Test[x_test_sep]
'''

#gbm0.fit(X, y)
#y_pred = gbm0.predict(X)
#y_predprod = gbm0.predict_proba(X)[:,1]
#print('Accuracy: %.4g' % metrics.accuracy_score(y.values, y_pred))
#print('AUC Score (Train): %f' % metrics.roc_auc_score(y, y_predprod) )
'''
param_grid = {'n_estimators':list(range(20, 81, 10)),
              'learning_rate': [0.2, 0.1, 0.05, 0.02, 0.01],
              'max_depth':[4, 5, 6, 7, 8],
              'min_samples_leaf': [3, 5, 9, 14],
              'max_features': [0.8, 0.5, 0.3, 0.1],
              'subsample':[0.6,0.7,0.75,0.8,0.85,0.9]}

#网格调参
n_estimators=60
'max_depth': 7
'min_samples_split': 1800
'min_samples_leaf': 70
{'max_features': 7}
'''

######################
gbm2 = GradientBoostingClassifier(learning_rate=0.01, n_estimators=400,max_depth=21,max_features=2, min_samples_leaf =60,
               min_samples_split =700, subsample=0.6, random_state=10)
gbm2.fit(X,y)
#y_pred = gbm2.predict(X)
y_predprob = gbm2.predict_proba(X_test)[:,1]
#y_predprob_sep = gbm2.predict_proba(X_test_sep)[:,1]
#print( "Accuracy : %.4g" % metrics.accuracy_score(y.values, y_pred))
#print ("AUC Score (Train): %f" % metrics.roc_auc_score(y, y_predprob))





f_result=open('0917-zong_result.txt', 'w')
for i in range(50000):
    y_auc = round(y_predprob[i], 4)
    print(Test[ID][i], y_auc)
    f_result.write(Test[ID][i])
    f_result.write(' ')
    f_result.write(str(y_auc))
    f_result.write('\n')
f_result.close()
'''
f_result=open('0913_max7_sep-zong_result.txt', 'w')
for i in range(50000):
    y_auc = round(y_predprob_sep[i], 4)
    print(Test_sep[ID][i], y_auc)
    f_result.write(Test_sep[ID][i])
    f_result.write(' ')
    f_result.write(str(y_auc))
    f_result.write('\n')
f_result.close()
    #f_result.write(Test[ID][i])'''

#print(y_pred)
#print(y_predprod)
#print('Accuracy: %.4g' % metrics.accuracy_score(y.values, y_pred))
#print('AUC Score (Train): %f' % metrics.roc_auc_score(y, y_predprod) )