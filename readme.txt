basicly we need to predict what is the probability that this customer will buy this product.


The dataset contains anonymized customers' shopping logs in the past 6 months before and on the "Double 11" day, and the information indicating whether they are loyal customers for given merchants (for training data only). The folder contains five files, with details listed below.

File descriptions

user_info.csv - customers' profiles, including their ages and genders
user_log.csv - customers' shopping logs in the past 6 months
train_label.csv - loyalty of customer and merchant pairs (for training)
test_label.csv - loyalty of customer and merchant pairs (for prediction)
sample_submission.csv - a sample submission file in the correct format
Data fields

user_info.csv (customer profile)

user_id - an anonymous id unique to a given customer
age_range - the customer' s age: 0 for <18; 1 for [18,24]; 2 for [25,29]; 3 for [30,34]; 4 for [35,39]; 5 for [40,49]; 6 for >= 50; 7 for unknown
gender - the customer's gender: 0 for female, 1 for male, 2 for unknown
user_log.csv (customer behavior log)

(note all the ids have been anonymized below)

user_id -  customer id
item_id -  item id
cat_id -  id of the product category that the item belongs to
merchant_id -  merchant id
brand_id - id of the brand of the item.
time_tamp - date when the action took place (format: mmdd)
action_type - an enumerate type {0, 1, 2, 3}, where 0 is for click, 1 is for add-to-cart, 2 is for purchase and 3 is for add-to-favourite
Training and Testing Data (train_label.csv, test_label.csv)

user_id#merchant_id - customer and merchant pair
prob - probability that the customer is loyal to the given merchant,  where 1 means loyal customer, 0 otherwise. This field is empty for test data.