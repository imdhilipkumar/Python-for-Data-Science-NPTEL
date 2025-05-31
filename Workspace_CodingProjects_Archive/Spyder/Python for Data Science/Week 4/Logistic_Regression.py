# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 07:30:15 2025

@author: DELL
"""
import os # for changing the workng directory
os.chdir(r"D:\Code-Hero-Hub\PYTHON\Data Science\Spyder\Python for Data Science\Week 4")

# import the Necessary Modules
import numpy as np # for Numerical operation
import pandas as pd # for the Handling the Data
import seaborn as sns # for the Data Visualization purpose

# Logistic Regression Model Necessary libraries

from sklearn.model_selection import train_test_split # To partition the Data
from sklearn.linear_model import LogisticRegression # To import the Logistic Regression model
from sklearn.metrics import accuracy_score, confusion_matrix # inport the performace matrix

# load the data
income_data = pd.read_csv("income.csv", na_values=[" ?"])
# copy the dataset for unchages the original dataset
data = income_data.copy()

data = pd.read_csv("income.csv", na_values=[" ?"])

# Explore the Data Analysis
# 1. get to know about the data
data.info()
# 2. check the missing values
data.isnull()
# sum the missing values
data.isnull().sum()

# summary of the data for the numerical dataset
data_summary = data.describe()
# summary for the categorical data
#data_summary_category = data.describe(include = "O")
#print(data_summary_category)

# Frequency distribution of specific columns:
data["JobType"].value_counts()
data["occupation"].value_counts()

# Data pre-processing
# 1. Identify missing values:
data.isnull().sum()
# 2. Filter rows with missing values:
missing_data = data[data.isnull().any(axis = 1)]
# 3. Remove rows with missing values:
data2 = data.dropna(axis = 0)
# 4. Create copies for further analysis:
data3 = data2.copy()
data4 = data3.copy()


# Convert categorical columns to numerical using one-hot encoding
#encoded_data = pd.get_dummies(data2, drop_first=True)
encode_data = pd.get_dummies(data2, drop_first = True )
# Calculate correlation
correlation = encode_data.corr()
print(correlation)

# Cross Table & Data Visualization
data2.columns
#Gender proportion table
gender = pd.crosstab(index = data["gender"], columns = "count", normalize =  True)

# Gender vs Salary Stats
gender_salary = pd.crosstab(index= data2["gender"], columns = data2["SalStat"], margins= True, normalize= True)

# Frequency Distribution of SalStat
SalStat = sns.countplot(data2["SalStat"])
# Histogram Distribution of Age
hist_age = sns.distplot(data2["age"], bins = 10, kde = False)
print(hist_age)

# box Plot for Age & Salary

box_age_Sal = sns.boxplot(x = "age", y = "SalStat", data = data2)
#*** Jobtype
JobType     = sns.countplot(y=data2['JobType'],hue = 'SalStat', data=data2)
job_salstat =pd.crosstab(index = data2["JobType"],columns = data2['SalStat'], margins = True, normalize =  'index')  
round(job_salstat*100,1)


#*** Education
Education   = sns.countplot(y=data2['EdType'],hue = 'SalStat', data=data2)
EdType_salstat = pd.crosstab(index = data2["EdType"], columns = data2['SalStat'],margins = True,normalize ='index')  
round(EdType_salstat*100,1)

#*** Occupation
Occupation  = sns.countplot(y=data2['occupation'],hue = 'SalStat', data=data2)
occ_salstat = pd.crosstab(index = data2["occupation"], columns =data2['SalStat'],margins = True,normalize = 'index')  
round(occ_salstat*100,1)

#*** Capital gain
sns.distplot(data2['capitalgain'], bins = 10, kde = False)

sns.distplot(data2['capitalloss'], bins = 10, kde = False)

# LOGISTIC REGRESSION
#Reindexing Salary Status Names
data2["SalStat"] = data2["SalStat"].map({" less than or equal to 50,000": 0, " greater than 50,000": 1})
print(data2['SalStat'])
#One-Hot Encoding (Converting Categorical Variables)

new_data = pd.get_dummies(data2, drop_first=True)

# Storing Column Names
column_list = list(new_data.columns)

# Separating Features and Target Variable 
features = list(set(column_list) - set(["SalStat"]))

#  Extracting  Feature (X) Variables and Target (y)
y = new_data["SalStat"].values

x = new_data[features].values
# Extracting Feature (X) Variables and Target (y)


# Splitting Data into Training and Testing Sets
train_x, test_x, train_y, test_y = train_test_split(x, y,test_size=0.3, random_state= 0)

# Creating Logistic Regression Model
logistic = LogisticRegression()

# Training the Model
logistic.fit(train_x, train_y)

# Model Coefficients & Intercept
logistic.coef_
logistic.intercept_

# Making Predictions on Test Data
prediction = logistic.predict(test_x)
print(prediction)

# Creating Confusion Matrix
confusion_matrix = confusion_matrix(test_y, prediction)
print(confusion_matrix)

# Calculating Model Accuracy
accuracy = accuracy_score(test_y, prediction)
print(accuracy)

#  Counting Misclassified Samples
print("MisClassified Samples : %d", (test_y != prediction).sum())

# LOGISTIC REGRESSION - REMOVING INSIGNIFICANT VARIABLES
#Reindexing Salary Status Names
data3["SalStat"] = data3["SalStat"].map({" less than or equal to 50,000": 0, " greater than 50,000": 1})

# Removing Insignificant Variables
col = ["gender", "JobType", "race", "nativecountry"]
new_data = data3.drop(col, axis = 1)
# One-Hot Encoding
new_data = pd.get_dummies(new_data, drop_first = True)
# Storing Column Names
column_list2 = list(new_data.columns)

# Separating Features and Target Variable

features2 = list(set(column_list2)-set(["SalStat"]))

# Extracting Target (y2) and Feature (x2) Variables
y2 = new_data["SalStat"].values
x2 = new_data[features2].values

# Splitting Data into Training and Testing Sets
train_x2, test_x2, train_y2, test_y2 = train_test_split(x2, y2, test_size=0.3, random_state=0)

# Creating Logistic Regression Model
logistic2 = LogisticRegression()

# Fitting the Model
logistic2.fit(train_x2, train_y2)

# Predicting on Test Data
prediction2 = logistic2.predict(test_x2)

accuracy2 = accuracy_score(test_y2,prediction2)

print('Misclassified samples: %d' % (test_y2 != prediction2).sum())
