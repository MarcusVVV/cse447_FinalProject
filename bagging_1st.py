from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn import cross_validation
#from sklearn.model_selection import cross_val_score
from sklearn.metrics import log_loss
import sklearn
#from xgboost import XGBClassifier
#from sklearn.model_selection import cross_val_score
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neural_network import MLPClassifier
import xgboost
from xgboost import XGBClassifier


dtrain = pd.read_csv('X_train_newfeature_part1_zuhe_2.csv', header=None, skiprows=[0]).as_matrix()
dtest = pd.read_csv('X_test_newfeature_part1_zuhe_2.csv',header=None, skiprows=[0]).as_matrix()
dlabel = pd.read_csv('train_label.csv', header=None, skiprows=[0]).as_matrix()

X = dtrain[:, 0:13]
y = dlabel[:, 1]
X_for_predict = dtest[:, 0:13]
#y_for_predict
Z = []#results
#seed = 100
seed = 100
test_size = 0.33
# split data into train and test sets
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=test_size, random_state=seed)
# specify parameters via map
print X_test


clf1 = XGBClassifier(max_depth=3, n_estimators=271)
clf2 = DecisionTreeClassifier(max_depth=10, random_state=10, max_leaf_nodes=10)
clf3 = KNeighborsClassifier(n_neighbors=250)
clf4 = MLPClassifier(hidden_layer_sizes=3000, alpha=1.5)
clf5 = RandomForestClassifier(n_estimators=160,max_leaf_nodes=40)

eclf1 = VotingClassifier(estimators=[('xgb', clf1), ('dt', clf2), ('knn', clf3), ('neural', clf4), ('rf', clf5)], voting='soft')

eclf1 = eclf1.fit(X_train, y_train)

y_pred = eclf1.predict_proba(X_test)
a = log_loss(list(y_test), eclf1.predict_proba(X_test))


print y_pred

print a

#logloss = log_loss(y_test, y_pred)
#print("logloss:" "%.6f%%" % logloss)
#clf = RandomForestClassifier(n_estimators=500)
