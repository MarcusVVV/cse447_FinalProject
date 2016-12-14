from __future__ import division
#import sklearn as sl
#import pandas as pd
import numpy as np

#from datetime import datetime, date
#from collections import defaultdict
#from sklearn.metrics import jaccard_similarity_score as jaccard
#from sklearn.feature_extraction.text import TfidfTransformer
#loading all data
#TFIDF = TfidfTransformer()
user_log = ("user_log.csv")
user_info = ("user_info.csv")
train_label = ("train_label.csv")
test_label = ("test_label.csv")

#creating output file
user_out_all = ("user_out_all.csv")
merchant_out_all = ("merchant_out_all.csv")

X_train = np.zeros(shape=(130365, 5))  #changes according to features number
y_train = np.zeros(shape=(130365, 1))
X_test = np.zeros(shape=(130501, 5))
y_test = np.zeros(shape=(130501, 1))

#for time stamp related features to use
def diff_days(s1, s2):
	date_format = "%m%d"
	a = datetime.strptime(s1, date_format)
	b = datetime.strptime(s2, date_format)
	delta = b - a
	return abs(delta.days)



def generate_features(user_log, user_info, train_label, test_label):
	train_ids = {}
	train_ids_user = {}
	train_ids_merchant = {}
	test_ids = {}
	test_ids_user = {}
	test_ids_merchant = {}
	#dictionares to store features
	user_bought_time = {}
	user_bought_time_in_1111 = {}
	user_favo_time = {}
	user_gender = {}
	user_age = {}
	user_action_times = {}
	user_action_dayaverage = {}
	user_action_day = {}
	user_action_day_number = {}
# 	# merchant_number_of_brand = {}
# 	# merchant_brands = {}
# 	# merchant_number_of_cat = {}
# 	# merchant_cat = {}
# 	# merchant_number_of_item = {}
# 	# merchant_item = {}
# 	# merchant_deals_times = {}
# 	# merchant_favo_times = {}
# 	# merchant_deals_times_in_1111 = {}




			#X_train.append(user_age[train_ids_user[row[0]]] + user_gender[train_ids_user[row[0]]] + user_bought_time[train_ids_user[row[0]]] + user_favo_time[train_ids_user[row[0]]] + user_bought_time_in_1111[train_ids_user[row[0]]] + merchant_number_of_brand[train_ids_merchant[row[0]]] +merchant_number_of_cat[train_ids_merchant[row[0]]] + merchant_number_of_item[train_ids_merchant[row[0]]] + merchant_deals_times[train_ids_merchant[row[0]]] +merchant_favo_times[train_ids_merchant[row[0]]] + merchant_deals_times_in_1111[train_ids_merchant[row[0]]])


			#X_test[e] = user_age[train_ids_user[row[0]]] + "," + user_gender[train_ids_user[row[0]]] +","+ user_bought_time[train_ids_user[row[0]]] + ","+user_favo_time[train_ids_user[row[0]]] +","+ user_bought_time_in_1111[train_ids_user[row[0]]] +","+ merchant_number_of_brand[train_ids_merchant[row[0]]] +","+merchant_number_of_cat[train_ids_merchant[row[0]]] +","+ merchant_number_of_item[train_ids_merchant[row[0]]] +","+ merchant_deals_times[train_ids_merchant[row[0]]] +","+merchant_favo_times[train_ids_merchant[row[0]]] +","+ merchant_deals_times_in_1111[train_ids_merchant[row[0]]]

	with open(user_out_all, "wb") as out_user, open(merchant_out_all, "wb") as out_merchant:
		#iterate through the log
		last_id = 0
		#last_id_merchant = 0
		#features = defaultdict(list)
		#features_id_user = {}  #store the pair of ids and features
		#features_id_merchant = {}
		for e, line in enumerate(open(user_info)):##e is counter(index)of row, line is the line
			if e > 0:   #skip first line
				row = line.strip().split(",")  #row[0] is just the user_id, not the pair
												#user_info's format is user_id|age_range|gender|
				if last_id != row[0] and e !=1:
					user_gender[row[0]] = row[2]
					user_age[row[0]] = row[1]


				if e % 100000 == 0:
					print e

		#i = -1
		#print len(list(enumerate(open(user_log))))

		for e, line in enumerate(open(user_log)):

		#	i += 1
			#print i
			if e > 0: #skip the header
				row = line.strip().split(",")



				if row[6] == "2":
					if user_bought_time.has_key(row[0]):
						user_bought_time[row[0]] += 1
					else:
						user_bought_time[row[0]] = 0
					if row[0] in user_action_times:
						user_action_times[row[0]] += 1
					else:
						user_action_times[row[0]] = 0
					# if merchant_deals_times.has_key(row[3]):
					# 	merchant_deals_times[row[3]] += 1
					# else:
					# 	merchant_deals_times[row[3]] = 0
					# if row[5] =="1111":
					# 	if merchant_deals_times_in_1111.has_key(row[3]):
					# 		merchant_deals_times_in_1111[row[3]] += 1
					# 	else:
					# 		merchant_deals_times_in_1111[row[3]] = 0
					if user_bought_time_in_1111.has_key(row[0]):
						user_bought_time_in_1111[row[0]] += 1
					else:
						user_bought_time_in_1111[row[0]] = 0
				if row[6] == "3":
					if user_favo_time.has_key(row[0]):
						user_favo_time[row[0]] += 1
					else:
						user_favo_time[row[0]] = 0
					if row[0] in user_action_times:
						user_action_times[row[0]] += 1
					else:
						user_action_times[row[0]] = 0
				if row[6] =="1":
					if row[0] in user_action_times:
						user_action_times[row[0]] += 1
					else:
						user_action_times[row[0]] = 0
				if row[6] =="0":
					if row[0] in user_action_times:
						user_action_times[row[0]] += 1
					else:
						user_action_times[row[0]] = 0
				if row[0] in user_action_day:
					user_action_day[row[0]].add(row[5])
				else:
					user_action_day[row[0]] = set()
				if row[0] in user_action_day_number:
					user_action_day_number[row[0]] = len(user_action_day[row[0]])
				else:
					user_action_day_number[row[0]] = 1
				#	if merchant_favo_times.has_key(row[3]):
				#		merchant_favo_times[row[3]] += 1
				#	else:
				#		merchant_favo_times[row[3]] = 0
# 				#
# 				# if merchant_brands.has_key(row[3]):
# 				# 	merchant_brands[row[3]].append(row[4])
# 				# else:
# 				# 	merchant_brands[row[3]] = []
# 				#
# 				# if merchant_cat.has_key(row[3]):
# 				# 	merchant_cat[row[3]].append(row[2])
# 				# else:
# 				# 	merchant_cat[row[3]] = []
# 				# if merchant_item.has_key(row[3]):
# 				# 	merchant_item[row[3]].append(row[1])
# 				# else:
# 				# 	merchant_item[row[3]] = []
# 				#
# 				#
# 				# if merchant_number_of_item.has_key(row[3]):
# 				# 	merchant_number_of_item[row[3]] = len(set(merchant_item[row[3]]))
# 				# else:
# 				# 	merchant_number_of_item[row[3]] = 0
# 				# if merchant_number_of_cat.has_key(row[3]):
# 				# 	merchant_number_of_cat[row[3]] = len(set(merchant_cat[row[3]]))
# 				# else:
# 				# 	merchant_number_of_cat[row[3]] = 0
# 				# if merchant_number_of_brand.has_key(row[3]):
# 				# 	merchant_number_of_brand[row[3]] = len(set(merchant_brands[row[3]]))
# 				# else:
# 				# 	merchant_number_of_brand[row[3]] = 0
			if e % 1000 == 0:
				print e
			#print "I am working! leave me alone!"
			#print user_age
		for e, line in enumerate(open(train_label)):
			if e > 0:
				row = line.strip().split(",")
				train_ids[row[0]] = row  # train pairs
				train_user = row[0].strip().split("#")[0]
				train_ids_user[row[0]] = train_user
				train_merchant = row[0].strip().split("#")[1]
				train_ids_merchant[row[0]] = train_merchant
				#
				user_action_dayaverage[train_ids_user[row[0]]] = user_action_times[train_ids_user[row[0]]] / user_action_day_number[train_ids_user[row[0]]]
				# print merchant_deals_times
				if train_ids_user[row[0]] in user_action_dayaverage:
					X_train[e][0] = user_action_dayaverage[train_ids_user[row[0]]]
				else:
					X_train[e][0] = 0
				if e % 1000 == 0:
					print e

		for e, line in enumerate(open(test_label)):
			if e > 0:
				row = line.strip().split(",")
				test_ids[row[0]] = row  # give v value test pairs
				test_user = row[0].strip().split("#")[0]
				test_ids_user[row[0]] = test_user
				test_merchant = row[0].strip().split("#")[1]
				test_ids_merchant[row[0]] = test_merchant
				user_action_dayaverage[test_ids_user[row[0]]] = user_action_times[test_ids_user[row[0]]]/user_action_day_number[test_ids_user[row[0]]]
	#print merchant_deals_times
				if test_ids_user[row[0]] in user_action_dayaverage:
					X_test[e][0] = user_action_dayaverage[test_ids_user[row[0]]]
				else:
					X_test[e][0] = 0

				if e % 1000 == 0:
					print e




if __name__ == '__main__':
	generate_features(user_log, user_info, train_label, test_label)
	np.savetxt("X_train_last_feature.csv", X_train,fmt='%10.3f', delimiter=",")
	np.savetxt("X_test_last_feature.csv", X_test, fmt='%10.3f',delimiter=",")







