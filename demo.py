##这个是波士顿房价预测的一个demo，原网址：http://blog.csdn.net/baixiaozhe/article/details/54409764
#那个作者还有第二部分，系列叫做： 用sklearn和tensorflow做boston房价的回归计算的比较：http://blog.csdn.net/baixiaozhe/article/details/54410313
# -*- coding: utf-8 -*-
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import GradientBoostingRegressor

#波士顿房价数据

boston = load_boston()
x = boston.data
y = boston.target
#print('波士顿数据', x.shape, len(x))
#print(x[:100])
#print('波士顿房价', y.shape, len(y))
#print(y[:100])

print('##################################')

#随机挑选
train_x_disorder, test_x_disorder, train_y_disorder, test_y_disorder = train_test_split(x, y, train_size=0.8, random_state=33)
#数据标准化
ss_x = preprocessing.StandardScaler()
train_x_disorder = ss_x.fit_transform(train_x_disorder)
test_x_disorder = ss_x.transform(test_x_disorder)

ss_y = preprocessing.StandardScaler()
train_y_disorder = ss_y.fit_transform(train_y_disorder.reshape(-1,1))
test_y_disorder = ss_y.transform(test_y_disorder.reshape(-1,1))

#多层感知机
#ravel()函数与flatten()函数类似，不过flatten返回拷贝值
model_mlp = MLPRegressor(solver='lbfgs', hidden_layer_sizes=(20,20,20), random_state=1)
model_mlp.fit(train_x_disorder, train_y_disorder.ravel())
mlp_score = model_mlp.score(test_x_disorder, test_y_disorder.ravel())
print('sklearn多层感知机-回归模型得分', mlp_score)
model_gbr_disorder = GradientBoostingRegressor()
model_gbr_disorder.fit(train_x_disorder, train_y_disorder.ravel())
gbr_score_disorder = model_gbr_disorder.score(test_x_disorder, test_y_disorder.ravel())
print('sklearn集成-回归模型的分', gbr_score_disorder)

'''
print('###############参数网格优选#############')

model_gbr_GridSearch = GradientBoostingRegressor()
#设置参数池 参考http://www.cnblogs.com/DjangoBlog/p/6201663.html
param_grid = {'n_estimators':range(20, 81, 10),
              'learning_rate': [0.2, 0.1, 0.05, 0.02, 0.01],
              'max_depth':[4, 6, 8],
              'min_samples_leaf': [3, 5, 9, 14],
              'max_features': [0.8, 0.5, 0.3, 0.1]}

#网格调参

from sklearn.model_selection import GridSearchCV
estimator = GridSearchCV(model_gbr_GridSearch, param_grid)
estimator.fit(train_x_disorder, train_y_disorder.ravel())
print("最优调参：", estimator.best_params_)
#{'learning_rate': 0.1, 'max_depth': 6, 'max_features': 0.5, 'min_samples_leaf': 14, 'n_estimators': 70}
print('调参后得分：', estimator.score(test_x_disorder, test_y_disorder.ravel()))

'''
#画图
model_gbr_best = GradientBoostingRegressor(learning_rate=0.1, max_depth=6, max_features=0.5, min_samples_leaf=14, n_estimators=70)
#model_gbr_best = GradientBoostingRegressor(learning_rate=0.2, max_depth=4, max_features=0.5, min_samples_leaf=3, n_estimators=60)
model_gbr_best.fit(train_x_disorder, train_y_disorder.ravel())
#使用默认参数的模型进行预测
gbr_pridict_disorder = model_gbr_disorder.predict(test_x_disorder)
#多层感知机
mlp_pridect_disorder = model_mlp.predict(test_x_disorder)
import matplotlib.pyplot as plt

#dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
fig = plt.figure(figsize=(20,3))
axes = fig.add_subplot(1,1,1)
line3,= axes.plot(range(len(test_y_disorder)), test_y_disorder, 'g', label='实际')
line1,= axes.plot(range(len(gbr_pridict_disorder)), gbr_pridict_disorder, 'b--', label='集成模型', linewidth=2)
line2,= axes.plot(range(len(mlp_pridect_disorder)), mlp_pridect_disorder, 'r--', label='多层感知机', linewidth=2)
axes.grid()
fig.tight_layout()
plt.legend(handles=[line1, line2, line3])
plt.title('sklearn回归模型')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'
plt.show()