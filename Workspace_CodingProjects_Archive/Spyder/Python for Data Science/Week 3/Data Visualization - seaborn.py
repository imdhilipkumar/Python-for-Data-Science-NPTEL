# import the necessary libaray
import os  # help to chagne the workng directory

os.chdir(r"D:\Code-Hero-Hub\PYTHON\Data Science\Spyder") # chaging the working directory
import pandas as pd # work with the data frames

import numpy as np # work with numerical operation

import matplotlib.pyplot as plt # work with the data  Visualization

import seaborn as sns

# import the data set
car_data = pd.read_csv("Toyota.csv")
data = pd.read_csv("Toyota.csv")

#Find out the null values and remove the extra column
data = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])

# Remove the null values
data.dropna(axis = 0, inplace = True)

# Scatter plot as seaborn
sns.set(style = "darkgrid")
# with Regression line
sns.regplot(x = data["Age"], y = data["Price"])
# without regression line
sns.regplot(x = data["Age"], y = data["Price"], fit_reg=False)

# plot using the marker
sns.regplot(x = data["Age"], y = data["Price"], marker = "*")
# include the anohter variable 
sns.lmplot(x="Age", y="Price", data=data, hue="FuelType", legend=True, palette="Set1")

# Histogram
sns.displot(data["Age"])
# without kernal density Estimate
sns.distplot(data["Price"], kde = False)
# fix the bins
sns.distplot(data["Price"], kde = False, bins = 5)
# Bar Plot
sns.countplot(x="FuelType", data=data)
# include the other categorical variables
sns.countplot(x="FuelType", data=data, hue="Automatic")


# Boxen plot with one categorical variable
sns.boxenplot(x="FuelType", y="Price", data=data)

# Boxen plot with an additional categorical variable (hue)
sns.boxenplot(x="FuelType", y="Price", hue="Automatic", data=data)

# Creating two plots (Boxplot and Histogram)
fig, (ax_box, ax_hist) = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={"height_ratios": [0.3, 0.7]})

# Boxplot
sns.boxplot(x=data["Price"], ax=ax_box)

# Histogram with Kernel Density Estimation (KDE)
sns.histplot(data["Price"], ax=ax_hist, kde=True)

plt.show()
# Pair plot data
sns.pairplot(data, hue="FuelType", palette="Set1")

