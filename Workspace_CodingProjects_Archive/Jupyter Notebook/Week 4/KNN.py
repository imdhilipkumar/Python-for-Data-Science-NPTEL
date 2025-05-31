# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 10:53:53 2025

@author: DELL
"""
import os 
os.chdir(r"D:\Code-Hero-Hub\PYTHON\Data Science\Spyder\Python for Data Science\Week 4")
# import the necessary Libraries
import pandas as pd # for Handle the Dataset
import numpy as np # for the numerical operation 
import seaborn as sns # for the advance data visualization
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# import the Dataset
data = pd.read_csv("income.csv", na_values=["?"])
# =============================================================================
# Data pre-processing
# =============================================================================
# checking the missing values
data.isnull().sum()

# if the dataset have the missing values store in the another variables
missing = data[data.isnull().any(axis = 1)]

# we need to remove the missing values to get the highly accuracy
data1 = data.dropna(axis = 0)

# Encode the Target Variables = Label Encoding
data1["SalStat"] = data1["SalStat"].map({" less than or equal to 50,000": 0, " greater than 50,000": 1})

# conver the Categorical variables into Dummy Variables
new_data = pd.get_dummies(data1, drop_first = True)

#Extracting Features & Target Variables
col_list = list(new_data.columns)
features = list(set(col_list) -set(["Salstat"]))

# get the variables
x = new_data[features].values
y = new_data["SalStat"].values

# Splitting Data into Training & Testing Sets
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.3, random_state=0)
# =============================================================================
# KNN
# =============================================================================
# KNN Model Training 
KNN_Classifier = KNeighborsClassifier(n_neighbors= 5)
#fit the train model
KNN_Classifier.fit(train_x, train_y)

# Predict the Model
prediction = KNN_Classifier.predict(test_x)
#print(prediction)

#  Evaluating Model Performance - using the Confusion Matrix
conf_matrix = confusion_matrix(test_y, prediction)
#print("Confusion matrix:\n", conf_matrix)

#Accuracy Score
accuracy = accuracy_score(test_y, prediction)
print(accuracy)

# Counts how many test cases were incorrectly classified.
print("Missclasifier\n", (test_y !=prediction).sum())

# Analyzing the Effect of Different K Values

miss_classifier_sample = []
for i in range(1, 20):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(train_x, train_y)
    prediction_i_knn = knn.predict(test_x)
    miss_classifier_sample.append((test_y != prediction_i_knn).sum())

print("Miss Classifier of different K values", miss_classifier_sample)

# =============================================================================
# END OF SCRIPT
# =============================================================================
