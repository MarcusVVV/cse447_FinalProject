#import sklearn as sl
#import pandas as pd
import numpy as np
#from datetime import datetime, date
#from collections import defaultdict
#from sklearn.metrics import jaccard_similarity_score as jaccard
import difflib
#from sklearn.feature_extraction.text import TfidfTransformer
#loading all data
#TFIDF = TfidfTransformer()
from math import*

def jaccard(x,y):
	intersection_cardinality = len(set.intersection(*[x, y]))
	union_cardinality = len(set.union(*[x, y]))
	return intersection_cardinality/float(union_cardinality)


user_log = ("user_log.csv")
user_info = ("user_info.csv")
train_label = ("train_label.csv")
test_label = ("test_label.csv")

#creating output file
user_out_all = ("user_out_all.csv")
merchant_out_all = ("merchant_out_all.csv")

X_train = np.zeros(shape=(130365, 4))  #changes according to features number
y_train = np.zeros(shape=(130365, 1))
X_test = np.zeros(shape=(130501, 4))
y_test = np.zeros(shape=(130501, 1))




def generate_features(user_log, user_info, train_label, test_label):
	train_ids = {}
	train_ids_user = {}
	train_ids_merchant = {}
	test_ids = {}
	test_ids_user = {}
	test_ids_merchant = {}
	#dictionares to store features
	# user_bought_time = {}
	# user_bought_time_in_1111 = {}
	# user_favo_time = {}
	# user_gender = {}
	# user_age = {}
	user_brands = {}
	user_item = {}
	user_cat = {}
	#merchant_number_of_brand = {}
	merchant_brands = {}
	#merchant_number_of_cat = {}
	merchant_cat = {}
	#merchant_number_of_item = {}
	merchant_item = {}
	#merchant_deals_times = {}
	#merchant_favo_times = {}
	#merchant_deals_times_in_1111 = {}
	user_merchant_item_simi = {}
	user_merchant_brand_simi = {}
	user_merchant_cat_simi = {}
	#user_merchant_age_simi = {}
	user_of_merchant = {}
	user_merchant_gender_simi = {}
	#user_gender_in_merchant = {}
	gender_0_in_merchant = {}
	gender_1_in_merchant = {}
	gender_2_in_merchant = {}
	has_never_bought_brand = {}
	has_never_bought_cat = {}
	gender_0 = set()
	gender_1 = set()
	gender_2 = set()

	for e, line in enumerate(open(user_info)):  ##e is counter(index)of row, line is the line
		if e > 0:  # skip first line
			row = line.strip().split(",")  # row[0] is just the user_id, not the pair
			if row[2] == "0":
				gender_0.add(row[0])
			if row[2] == "1":
				gender_1.add(row[0])
			if row[2] == "2":
				gender_2.add(row[0])

		if e % 100000 == 0:
			print e




	for e, line in enumerate(open(user_log)):
	#	i += 1
		#print i
		if e > 0: #skip the header
			row = line.strip().split(",")
			#date_diff_days = diff_days(row[5], "1111")  # days between bought time and 1111
			#if last_id != row[0] and e != 1:
			#if row[0] in train_ids_user.values() or row[0] in test_ids_user.values() or row[3] in train_ids_merchant.values() or row[3] in test_ids_merchant.values():
			if row[6] == "2":
				# if user_bought_time.has_key(row[0]):
				# 	user_bought_time[row[0]] += 1
				# else:
				# 	user_bought_time[row[0]] = 0
				if row[3] in user_of_merchant:
					user_of_merchant[row[3]].add(row[0])
				else:
					user_of_merchant[row[3]] = set()

				if row[0] in gender_0:
					if row[3] in gender_0_in_merchant:
						gender_0_in_merchant[row[3]].add(row[0])
					else:
						gender_0_in_merchant[row[3]] = set()

				if row[0] in gender_1:
					if row[3] in gender_1_in_merchant:
						gender_1_in_merchant[row[3]].add(row[0])
					else:
						gender_1_in_merchant[row[3]] = set()

				if row[0] in gender_2:
					if row[3] in gender_2_in_merchant:
						gender_2_in_merchant[row[3]].add(row[0])
					else:
						gender_2_in_merchant[row[3]] = set()

				if row[0] in user_item:
					user_item[row[0]].add(row[1])
				else:
					user_item[row[0]] = set()
				if row[0] in user_cat:
					user_cat[row[0]].add(row[2])
				else:
					user_cat[row[0]] = set()
				if row[0] in user_brands:
					user_brands[row[0]].add(row[4])
				else:
					user_brands[row[0]] = set()

			if merchant_brands.has_key(row[3]):
				merchant_brands[row[3]].add(row[4])
			else:
				merchant_brands[row[3]] = set()
			if merchant_cat.has_key(row[3]):
				merchant_cat[row[3]].add(row[2])
			else:
				merchant_cat[row[3]] = set()
			if merchant_item.has_key(row[3]):
				merchant_item[row[3]].add(row[1])
			else:
				merchant_item[row[3]] = set()

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

			user_merchant_brand_simi[row[0]] = jaccard(user_brands[train_ids_merchant[row[0]]], merchant_brands[train_ids_merchant[row[0]]])
			user_merchant_item_simi[row[0]] = jaccard(user_item[train_ids_merchant[row[0]]],merchant_item[train_ids_merchant[row[0]]])
			user_merchant_cat_simi[row[0]] = jaccard(user_cat[train_ids_merchant[row[0]]], merchant_cat[train_ids_merchant[row[0]]])
			#user_merchant_age_simi[row[0]] = jaccard()
			if train_user in gender_0:
				user_merchant_gender_simi[row[0]] = jaccard(gender_0_in_merchant[train_ids_merchant[row[0]]],user_of_merchant[train_ids_merchant[row[0]]])
			if train_user in gender_1:
				user_merchant_gender_simi[row[0]] = jaccard(gender_1_in_merchant[train_merchant],user_of_merchant[train_merchant])
			if train_user in gender_2:
				user_merchant_gender_simi[row[0]] = jaccard(gender_2_in_merchant[train_merchant],user_of_merchant[train_merchant])

			# output format:simi of item, simi of brand, simi of cat,simi of gender
			#print train_ids_merchant[row[0]]
			# X_train.append(user_age[train_ids_user[row[0]]]+user_gender[train_ids_user[row[0]]]+user_bought_time[train_ids_user[row[0]]]+user_favo_time[train_ids_user[row[0]]]+user_bought_time_in_1111[train_ids_user[row[0]]]+merchant_number_of_brand[train_ids_merchant[row[0]]]+merchant_number_of_cat[train_ids_merchant[row[0]]]+merchant_number_of_item[train_ids_merchant[row[0]]]+merchant_deals_times[train_ids_merchant[row[0]]]+merchant_favo_times[train_ids_merchant[row[0]]]+merchant_deals_times_in_1111[train_ids_merchant[row[0]]])
			# X_train[e] = user_age[train_ids_user[row[0]]] + "," + user_gender[train_ids_user[row[0]]] + "," + \
			#              user_bought_time[train_ids_user[row[0]]] + "," + user_favo_time[train_ids_user[row[0]]] + "," + \
			#              user_bought_time_in_1111[train_ids_user[row[0]]] + "," + merchant_number_of_brand[
			# 	             train_ids_merchant[row[0]]] + "," + merchant_number_of_cat[
			# 	             train_ids_merchant[row[0]]] + "," + merchant_number_of_item[
			# 	             train_ids_merchant[row[0]]] + "," + merchant_deals_times[
			# 	             train_ids_merchant[row[0]]] + "," + merchant_favo_times[train_ids_merchant[row[0]]] + "," + \
			#              merchant_deals_times_in_1111[train_ids_merchant[row[0]]]
			if row[0] in user_merchant_item_simi:
				X_train[e][0] = user_merchant_item_simi[row[0]]
			else:
				X_train[e][0] = 0
			if row[0] in user_merchant_brand_simi:
				X_train[e][1] = user_merchant_brand_simi[row[0]]
			else:
				X_train[e][1] = 0
			if row[0] in user_merchant_cat_simi:
				X_train[e][2] = user_merchant_cat_simi[row[0]]
			else:
				X_train[e][2] = 0
			if row[0] in user_merchant_gender_simi:
				X_train[e][3] = user_merchant_gender_simi[row[0]]
			else:
				X_train[e][3] = 0

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

			user_merchant_brand_simi[row[0]] = jaccard(user_brands[test_user], merchant_brands[test_merchant])
			user_merchant_item_simi[row[0]] = jaccard(user_item[test_user], merchant_item[test_merchant])
			user_merchant_cat_simi[row[0]] = jaccard(user_cat[test_user], merchant_cat[test_merchant])
			if test_user in gender_0:
				user_merchant_gender_simi[row[0]] = jaccard(gender_0_in_merchant[test_merchant], user_of_merchant[test_merchant])

			if row[0] in user_merchant_item_simi:
				X_test[e][0] = user_merchant_item_simi[row[0]]
			else:
				X_test[e][0] = 0
			if row[0] in user_merchant_brand_simi:
				X_test[e][1] = user_merchant_brand_simi[row[0]]
			else:
				X_test[e][1] = 0
			if row[0] in user_merchant_cat_simi:
				X_test[e][2] = user_merchant_cat_simi[row[0]]
			else:
				X_test[e][2] = 0
			if row[0] in user_merchant_gender_simi:
				X_test[e][3] = user_merchant_gender_simi[row[0]]
			else:
				X_test[e][3] = 0
			if e % 1000 == 0:
				print e




if __name__ == '__main__':
	generate_features(user_log, user_info, train_label, test_label)
	np.savetxt("X_train_newfeature_intersection_test.csv", X_train, fmt='%10.4f', delimiter=",")
	np.savetxt("X_test_newfeature_intersection_test.csv", X_test, fmt='%10.4f', delimiter=",")







