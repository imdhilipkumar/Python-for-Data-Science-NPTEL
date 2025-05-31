# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 21:55:17 2025

@author: DELL
"""
# Working with the file directory
import os
os.chdir(r"D:\Code-Hero-Hub\PYTHON\Data Science\Spyder\Python for Data Science\Week 4")

# Importing the Necessary Libraries
import pandas as pd  # For handling the dataset
import numpy as np  # For numerical operations
import seaborn as sns

# Setting the dimension for plot for better visualization
sns.set(rc={"figure.figsize": (11.7, 8.27)})

# Read the data
car_data = pd.read_csv("cars_sampled.csv")

# Copy the dataset
data = car_data.copy()
data1 = data.copy()

# Display the dataset structure
data.info()

# Summarize the data
b = data.describe()
pd.set_option('display.float_format', lambda x: '%.3f' % x)
data.describe()

# Display all columns
pd.set_option("display.max_columns", 500)
data.describe()

# Drop unwanted columns for better accuracy
col = ["name", "dateCrawled", "dateCreated", 'postalCode', 'lastSeen']
data = data.drop(col, axis=1)

# Remove duplicates
data.drop_duplicates(keep="first", inplace=True)

# Data Cleaning
# 1. Checking for missing values
data.isnull().sum()
# 2. Analyzing yearOfRegistration
year_wise_count = data["yearOfRegistration"].value_counts().sort_index()

sum(data['yearOfRegistration'] > 2018)
sum(data['yearOfRegistration'] < 1950)

# Plots a scatter plot of yearOfRegistration vs price
sns.regplot(x="yearOfRegistration", y="price", fit_reg=False, data=data)

# 3. Analyzing price
price_count = data["price"].value_counts().sort_index()

# Plots the distribution (histogram) of car prices
sns.histplot(data["price"])
data["price"].describe()
sns.boxplot(y=data["price"])

print(sum(data["price"] > 150000))
print(sum(data["price"] < 100))

# 4. Analyzing powerPS
power_count = data["powerPS"].value_counts().sort_index()

# Histogram for the PowerPS
sns.histplot(data["powerPS"])

# Working range of data
data = data[
    (data.yearOfRegistration <= 2018)
    & (data.yearOfRegistration >= 1950)
    & (data.price >= 100)
    & (data.price <= 150000)
    & (data.powerPS >= 10)
    & (data.powerPS <= 500)]

# Converting the month of registration to a fraction of a year
data["monthOfRegistration"] /= 12

# Creating a new column 'Age'
data["Age"] = (2018 - data["yearOfRegistration"]) + data["monthOfRegistration"]

# Rounding the 'Age' column to two decimal places
data["Age"] = round(data["Age"], 2)

# Descriptive statistics for 'Age'
data["Age"].describe()

# Dropping unnecessary columns
data = data.drop(columns=["yearOfRegistration", "monthOfRegistration"], axis=1)

# Visualizing parameters
# Age
sns.histplot(data["Age"])
sns.boxplot(y=data["Age"])

# Price
sns.histplot(data["price"])
sns.boxplot(y=data["price"])

# PowerPS
sns.histplot(data["powerPS"])
sns.boxplot(y=data["powerPS"])

# Visualizing parameters after narrowing working range
# Age vs price
sns.regplot(x="Age", y="price", scatter=True, fit_reg=False, data=data)

# PowerPS vs price
sns.regplot(x="powerPS", y="price", scatter=True, fit_reg=False, data=data)

# Visualization Analysis
# Variables for vehicleType
data["vehicleType"].value_counts()
pd.crosstab(data["vehicleType"], columns="count", normalize=True)
sns.countplot(x="vehicleType", data=data)
sns.boxplot(x="vehicleType", y="price", data=data)

# Variables for gearbox
data["gearbox"].value_counts()
pd.crosstab(data["gearbox"], columns="count", normalize=True)
sns.countplot(x="gearbox", data=data)
sns.boxplot(x="gearbox", y="price", data=data)

# Variables for model
data["model"].value_counts()
pd.crosstab(data["model"], columns="count", normalize=True)
sns.countplot(x="model", data=data)
sns.boxplot(x="model", y="price", data=data)

# Variables for kilometer
data["kilometer"].value_counts()
pd.crosstab(data["kilometer"], columns="count", normalize=True)
sns.countplot(x="kilometer", data=data)
sns.boxplot(x="kilometer", y="price", data=data)

# Variables for fuelType
data["fuelType"].value_counts()
pd.crosstab(data["fuelType"], columns="Counts", normalize="columns")
sns.countplot(x="fuelType", data=data)
sns.boxplot(x="fuelType", y="price", data=data)

# Variables for brand
data["brand"].value_counts()
pd.crosstab(data["brand"], columns="count", normalize=True)
sns.countplot(x="brand", data=data)
sns.boxplot(x="brand", y="price", data=data)

# Variables for notRepairedDamage
data["notRepairedDamage"].value_counts()
pd.crosstab(data["notRepairedDamage"], columns="count", normalize=True)
sns.countplot(x="notRepairedDamage", data=data)
sns.boxplot(x="notRepairedDamage", y="price", data=data)

# Removing insignificant variables
col = ["seller", "offerType", "abtest"]
data = data.drop(columns=col, axis=1)
data_copy = data.copy()

# Correlation Calculation:
data_select = data.select_dtypes(exclude=[object])
corr_data = data_select.corr()
round(corr_data, 3)
data_select.corr().loc[:, 'price'].abs().sort_values(ascending=False)[1:]

# To build a Linear Regression and Random Forest model
# Omitting Missing Values:
data_omit = data.dropna(axis=0)

# Converting Categorical Variables to Dummy Variables:
data_omit = pd.get_dummies(data_omit, drop_first=True)

# Importing necessary libraries
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Assuming data_omit and cars are already loaded

# Separating input and output features
x1 = data_omit.drop(['price'], axis='columns', inplace=False)
y1 = data_omit['price']

# Handling zero or negative values for logarithmic transformation
y1 = np.log1p(y1)  # Adding 1 to avoid log(0) or negative values

# Splitting data into train and test
X_train, X_test, y_train, y_test = train_test_split(x1, y1, test_size=0.3, random_state=3)

# Baseline model
base_pred = np.mean(y_test)
base_pred = np.repeat(base_pred, len(y_test))
base_rmse = np.sqrt(mean_squared_error(y_test, base_pred))

# Linear Regression
lgr = LinearRegression(fit_intercept=True)
model_lin1 = lgr.fit(X_train, y_train)
cars_predictions_lin1 = lgr.predict(X_test)
lin_rmse1 = np.sqrt(mean_squared_error(y_test, cars_predictions_lin1))
r2_lin_test1 = model_lin1.score(X_test, y_test)
r2_lin_train1 = model_lin1.score(X_train, y_train)

# Residual plot
residuals1 = y_test - cars_predictions_lin1
sns.regplot(x=cars_predictions_lin1, y=residuals1, scatter=True, fit_reg=False)

# Random Forest
rf = RandomForestRegressor(n_estimators=100, max_features=None, max_depth=100, 
                           min_samples_split=10, min_samples_leaf=4, random_state=1)
model_rf1 = rf.fit(X_train, y_train)
cars_predictions_rf1 = rf.predict(X_test)
rf_rmse1 = np.sqrt(mean_squared_error(y_test, cars_predictions_rf1))
r2_rf_test1 = model_rf1.score(X_test, y_test)
r2_rf_train1 = model_rf1.score(X_train, y_train)

# Handling missing values in cars dataset imputed data
cars_imputed = data.apply(lambda x: x.fillna(x.median()) if x.dtype == 'float' else x.fillna(x.mode().iloc[0]))
cars_imputed = pd.get_dummies(cars_imputed, drop_first=True)

# Separating input and output
x2 = cars_imputed.drop(['price'], axis='columns', inplace=False)
y2 = np.log1p(cars_imputed['price'])

# Train-test split
X_train1, X_test1, y_train1, y_test1 = train_test_split(x2, y2, test_size=0.3, random_state=3)

# Baseline model
base_pred = np.mean(y_test1)
base_pred = np.repeat(base_pred, len(y_test1))
base_rmse_imputed = np.sqrt(mean_squared_error(y_test1, base_pred))

# Linear Regression
model_lin2 = lgr.fit(X_train1, y_train1)
cars_predictions_lin2 = lgr.predict(X_test1)
lin_rmse2 = np.sqrt(mean_squared_error(y_test1, cars_predictions_lin2))
r2_lin_test2 = model_lin2.score(X_test1, y_test1)
r2_lin_train2 = model_lin2.score(X_train1, y_train1)

# Random Forest
model_rf2 = rf.fit(X_train1, y_train1)
cars_predictions_rf2 = rf.predict(X_test1)
rf_rmse2 = np.sqrt(mean_squared_error(y_test1, cars_predictions_rf2))
r2_rf_test2 = model_rf2.score(X_test1, y_test1)
r2_rf_train2 = model_rf2.score(X_train1, y_train1)

# Final output
print("Metrics for models built from data where missing values were omitted")
print(f"R squared value for train from Linear Regression: {r2_lin_train1}")
print(f"R squared value for test from Linear Regression: {r2_lin_test1}")
print(f"R squared value for train from Random Forest: {r2_rf_train1}")
print(f"R squared value for test from Random Forest: {r2_rf_test1}")
print(f"Base RMSE: {base_rmse}")
print(f"Linear Regression RMSE: {lin_rmse1}")
print(f"Random Forest RMSE: {rf_rmse1}")

print("\nMetrics for models built from data where missing values were imputed")
print(f"R squared value for train from Linear Regression: {r2_lin_train2}")
print(f"R squared value for test from Linear Regression: {r2_lin_test2}")
print(f"R squared value for train from Random Forest: {r2_rf_train2}")
print(f"R squared value for test from Random Forest: {r2_rf_test2}")
print(f"Base RMSE: {base_rmse_imputed}")
print(f"Linear Regression RMSE: {lin_rmse2}")
print(f"Random Forest RMSE: {rf_rmse2}")
