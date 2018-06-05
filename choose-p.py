# -*- coding: utf-8 -*-
# @Time    : 2017/9/11 13:46
# @Author  : Lxy
# @Site    : 
# @File    : choose-p.py
# @Software: PyCharm
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV

import matplotlib.pylab as plt

train = pd.read_csv('train_modified.csv')
target = "Disbursed"
IDcol = 'ID'
train["Disbursed"].value_counts()
#0:19680; 1:320

x_columns = [x for x in train.columns if x not in [target, IDcol]]
X = train[x_columns]
y = train['Disbursed']
'''
gbm0 = GradientBoostingClassifier(random_state=10)
gbm0.fit(X, y)
y_pred = gbm0.predict(X)
y_predprod = gbm0.predict_proba(X)[:,1]
print('Accuracy: %.4g' % metrics.accuracy_score(y.values, y_pred))
print('AUC Score (Train): %f' % metrics.roc_auc_score(y, y_predprod) )

#############以下为网格参数寻优步骤###############

param_test1 = {'n_estimators': list(range(20, 81, 10))}
gsearch1 = GridSearchCV(estimator=GradientBoostingClassifier(learning_rate=0.1, min_samples_split=300,
                                                             min_samples_leaf=20, max_depth=8, max_features='sqrt',
                                                             subsample=0.8, random_state=10)
                        , param_grid=param_test1, scoring='roc_auc',iid=False,cv=5)
gsearch1.fit(X, y)
print(gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_)

#######n_estimators最佳为60：0.8175146087398375#########

#原始网址：http://www.cnblogs.com/pinard/p/6143927.html
#09.10看到这里，下周有时间继续

param_test2 = {'max_depth':list(range(3,14,2)), 'min_samples_split': list(range(100, 801, 200))}
gsearch2 = GridSearchCV(estimator=GradientBoostingClassifier(learning_rate=0.1, n_estimators=60, min_samples_leaf=20,
                                                             max_features='sqrt', subsample=0.8, random_state=10),
                        param_grid=param_test2, scoring='roc_auc', iid=False, cv=5)
gsearch2.fit(X, y)
print(gsearch2.grid_scores_, gsearch2.best_params_, gsearch2.best_score_)

#########{'max_depth': 7, 'min_samples_split': 300} 0.8213724275914632#######

param_test3 = {'min_samples_split': list(range(800, 1900, 200)), 'min_samples_leaf': list(range(10, 61, 10))}
gsearch3 = GridSearchCV(estimator=GradientBoostingClassifier(learning_rate=0.1, n_estimators=60, max_depth=7,
                                                             max_features='sqrt', subsample=0.8, random_state=10),
                        param_grid=param_test3, scoring='roc_auc', iid=False, cv=5)
gsearch3.fit(X, y)
print(gsearch3.grid_scores_, gsearch3.best_params_, gsearch3.best_score_)
###########{'min_samples_leaf': 60, 'min_samples_split': 1200} 0.8222032996697154#############

param_test4 = {'max_features': list(range(7,20,2))}
gsearch4 = GridSearchCV(estimator=GradientBoostingClassifier(learning_rate=0.1, n_estimators=60, max_depth=7,
                                                             min_samples_leaf=60, min_samples_split=1200, subsample=0.8,
                                                             random_state=10),
                        param_grid=param_test4, scoring='roc_auc', iid=False, cv=5)
gsearch4.fit(X, y)
print(gsearch4.grid_scores_, gsearch4.best_params_, gsearch4.best_score_)
#############{'max_features': 9} 0.822412506351626##############



#############参数寻优结束###############

gbm1 = GradientBoostingClassifier(learning_rate=0.1, n_estimators=60, max_depth=7, min_samples_leaf=60,
                                  min_samples_split=1200, max_features='sqrt', subsample=0.8,
                                  random_state=10)
gbm1.fit(X,y)
y_pred = gbm1.predict(X)
y_predprod = gbm1.predict_proba(X)[:,1]
print('准确率：%.4g'% metrics.accuracy_score(y.values, y_pred))
print('AUC得分： %f'% metrics.roc_auc_score(y, y_predprod))

param_test5 = {'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]}
gsearch5 = GridSearchCV(estimator=GradientBoostingClassifier(learning_rate=0.1, n_estimators=60, max_depth=7, min_samples_leaf=60,
                                                             min_samples_split=1200, max_features=9, random_state=10),
                        param_grid=param_test5, scoring='roc_auc', iid=False, cv=5)
gsearch5.fit(X,y)
print(gsearch5.grid_scores_, gsearch5.best_params_, gsearch5.best_score_)
###############{'subsample': 0.7} 0.8234378969766262###############
'''

gbm2 = GradientBoostingClassifier(learning_rate=0.05, n_estimators=120, max_depth=7, min_samples_leaf=60,
                                  min_samples_split=1200, max_features=9, subsample=0.7, random_state=10)
gbm2.fit(X,y)
y_pred = gbm2.predict(X)
y_predprob = gbm2.predict_proba(X)[:,1]
print('Accuracy: %.4g'% metrics.accuracy_score(y.values, y_pred))
print('AUC Score (Train): %f' % metrics.roc_auc_score(y, y_predprob))



