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
from sklearn.ensemble import ExtraTreesClassifier, VotingClassifier
from sklearn.neural_network import MLPClassifier
import xgboost
from xgboost import XGBClassifier
from mlxtend.classifier import EnsembleVoteClassifier




dtrain = pd.read_csv('X_train_newfeature_part1_zuhe_2.csv', header=None, skiprows=[0]).as_matrix()
dtest = pd.read_csv('X_test_newfeature_part1_zuhe_2.csv',header=None, skiprows=[0]).as_matrix()
dlabel = pd.read_csv('train_label.csv',header=None, skiprows=[0]).as_matrix()

X = dtrain[:, 0:12]
y = dlabel[:, 1]
X_for_predict = dtest[:, 0:12]
Z = []#results

clf1 = XGBClassifier(max_depth=3, n_estimators=271)
#clf2 = DecisionTreeClassifier(max_depth=10, random_state=10, max_leaf_nodes=10)
clf3 = KNeighborsClassifier(n_neighbors=250)
#clf4 = MLPClassifier(hidden_layer_sizes=3000, alpha=1.5)
#clf5 = RandomForestClassifier(n_estimators=160,max_leaf_nodes=40)

eclf1 = EnsembleVoteClassifier(clfs=[clf1,clf3], weights=[2, 1], voting='soft')

eclf1 = eclf1.fit(X, y)
y_pred = eclf1.predict_proba(X_for_predict)
print y_pred



# make prediction
for i in xrange(130500):
	y_test_out = y_pred[i][1]
	Z.append(y_test_out)


np.savetxt("submission_EnsembleVoting.csv", Z, fmt='%10.4f',delimiter=",")
print "I just finished my job here"
