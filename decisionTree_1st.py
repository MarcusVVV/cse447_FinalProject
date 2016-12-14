from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
from sklearn import cross_validation
#from sklearn.model_selection import cross_val_score
from sklearn.metrics import log_loss
import sklearn
#from xgboost import XGBClassifier
#from sklearn.model_selection import cross_val_score


dtrain = pd.read_csv('X_train_newfeature_part1_zuhe_2.csv', header=None, skiprows=[0]).as_matrix()
dtest = pd.read_csv('X_test_newfeature_part1_zuhe_2.csv',header=None, skiprows=[0]).as_matrix()
dlabel = pd.read_csv('train_label.csv', header=None, skiprows=[0]).as_matrix()

X = dtrain[:, 0:12]
y = dlabel[:, 1]
X_for_predict = dtest[:, 0:12]
#y_for_predict
Z = []#results
#seed = 100
seed = 100
test_size = 0.33
# split data into train and test sets
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=test_size, random_state=seed)
# specify parameters via map
print X_test
clf = DecisionTreeClassifier(max_depth=10, random_state=10, max_leaf_nodes=8)  # optimal == 8
clf.fit(list(X_train), list(y_train))
y_pred = clf.predict_proba(X_test)
#a = cross_val_score(clf,y_train,y_pred)
a = log_loss(list(y_test), clf.predict_proba(X_test))

print y_pred

print a

#logloss = log_loss(y_test, y_pred)
#print("logloss:" "%.6f%%" % logloss)