import os  # help to chagne the workng directory

os.chdir(r"D:\Code-Hero-Hub\PYTHON\Data Science\Spyder") # chaging the working directory
import pandas as pd # work with the data frames

import numpy as np # work with numerical operation
# reading the dataset
data = pd.read_csv("Toyota.csv", index_col=0, na_values=["??", "????"])
# copying the dataset
data1 = data.copy()
data2 = data.copy()
data3 = data.copy()

# check the null values present in the data
data.isnull().sum()
data.isna().sum()

#collect the missing values in missing variables
missing_data = data[data.isnull().any(axis = 1)]

des = data.describe()

# Taking the numerical variables - 1. Age, 2.HP, 3.KM
data["Age"].mean()

# fill up the missing values

data1["Age"].fillna(data1["Age"].mean(), inplace = True)

# like wise HP & KM
# we take the mean and median value based on the dataset value like wiht is less compare of both , we took the less value to analyis
data1["HP"].median()
# fill up the na vlaues
data1["HP"].fillna(data1["HP"].mean(), inplace = True)

data1["KM"].median()
# fill up the na vlaues
data1["KM"].fillna(data1["KM"].median(), inplace = True)

# check the dataset

data1.isnull().sum()

# get in to the Categorical variables
data1["FuelType"].value_counts()
# find the mode
data1["FuelType"].mode()

# fill up the na values

data1["FuelType"].fillna(data1["FuelType"].mode()[0], inplace = True)
data1["FuelType"].fillna(data1["FuelType"].value_counts().index[0], inplace = True)
# like wise we check the Metcolor
data1["MetColor"].value_counts()
# find the mode
data1["MetColor"].mode()
# fill up themissing Values 
data1["MetColor"].fillna(data1["MetColor"].value_counts().index[0], inplace =True)
data1.isnull().sum()

# filling the missing values using the lambda functions
data_na = data2.isna().sum()
data2 = data2.apply(lambda x:x.fillna(x.mean())\
                    if x.dtypes == "float" else\
                        x.fillna(x.value_counts().index[0]))
data2.isnull().sum()

d3 = data3.isnull().sum()
# filling the missing values using the lambda functions uning mode 
data3 = data2.apply(lambda x:x.fillna(x.median())\
                    if x.dtype == "float" else\
                        x.fillna(x.mode()[0]))
data3.isna().sum()

