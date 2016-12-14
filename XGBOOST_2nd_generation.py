import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.metrics import log_loss
from xgboost import XGBClassifier

# read in data
dtrain = pd.read_csv('X_train_newfeature_part1_zuhe_2.csv', header=None, skiprows=[0]).as_matrix()
dtest = pd.read_csv('X_test_newfeature_part1_zuhe_2.csv',header=None, skiprows=[0]).as_matrix()
dlabel = pd.read_csv('train_label.csv',header=None, skiprows=[0]).as_matrix()

X = dtrain[:, 0:12]
y = dlabel[:, 1]
X_for_predict = dtest[:, 0:12]
#y_for_predict
Z = []#results
#seed = 100
#test_size = 0.33
# split data into train and test sets
#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=test_size, random_state=seed)
# specify parameters via map
#print X_test
model = xgb.XGBClassifier(max_depth=3, n_estimators=390)
model.fit(X, y)
y_pred = model.predict_proba(X_for_predict)
print y_pred
#logloss = model.evals_result()
#predictions = [round(value) for value in y_pred]
#logloss = log_loss(y_test, y_pred)
#print("logloss:" "%.3f%%" % logloss)



# make prediction
for i in xrange(130500):
	y_test_out = y_pred[i][1]
	Z.append(y_test_out)


np.savetxt("submission_XGBOOST.csv", Z, fmt='%10.3f',delimiter=",")
print "I just finished my job here"