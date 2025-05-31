# to change the working dirctory
import os 
os.chdir(r"D:\Code-Hero-Hub\PYTHON\Data Science\Spyder")

# importing the necessary packages
import pandas as pd # work with  Dataframes
import numpy as np # for numberical computation

# importing the dataset

car_data =pd.read_csv("Toyota.csv", index_col=0)
car_data1 = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])
car_data2 = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])
print(car_data)
# Attributes of Data
car_data.index # to give the rows label

car_data.columns # gives the column names

car_data.size #give the total size of the data rowx * column

car_data.shape # check how many rows and column

car_data.memory_usage # how much single data data use for individual elements

car_data.ndim # check the dimension of the data set 2D or 3D

# Indexing & Selecting the Data

car_data.loc[:,"FuelType"]

# check the Datatypes of each column
car_data.dtypes

# count the unique Data type
car_data.dtypes.unique()

# Selecting the dta based on Data type
car_data.select_dtypes(exclude=[object])

# Summary of the Data
car_data.info()
car_data1.info()
# Convert vriable data tyes
car_data1["MetColor"] = car_data1["MetColor"].astype("object")
car_data1["Automatic"] = car_data1["Automatic"].astype("object")
car_data.info()
car_data1.info()

# Checking the Total Bytes consuming the elemnt of each column

car_data["FuelType"].nbytes

car_data["FuelType"].astype("category").nbytes

# Cleanng the Error values to Desire Value

np.unique(car_data1["Doors"])

# Replace the value

car_data1["Doors"].replace("three", 3, inplace = True)
car_data1["Doors"].replace("four", 4, inplace = True)
car_data1["Doors"].replace("five", 5, inplace = True)
# check the Data type
car_data1["Doors"] =car_data1["Doors"].astype("int64")
# Correct value replacement
#car_data1["Doors"].replace({"five": 5, "four": 4, "three": 3}, inplace=True)

# Convert data type to int64
#car_data1["Doors"] = car_data1["Doors"].astype("int64")
print(car_data1.info())

# check the Missing value
car_data1.isnull().sum()

# Insert the new columne
car_data1.insert(10, "Price Class", "")
car_data1.insert(11, "Age Convert", "")
car_data1.insert(12, "KM per Month", "")
car_data2.insert(10, "KM per Month", "")

# Using the for loop to insert the Data
for i in range(0, len(car_data1["Price"]), 1):
    if car_data1["Price"][i] <= 8450:
        car_data1["Price Class"][i] = "Low"
    elif car_data1["Price"][i] >= 11950:
        car_data1["Price Class"][i] = "High"
    else:
        car_data1["Price Class"][i] = "Medium"

# Check the unique value

car_data1["Price Class"].value_counts()

# Define the function conver age in to months

def value_converter(val):
    val_converter = val/12
    return val_converter

# Add the value in to Age converter and round the value to get the proper value
car_data1["Age Convert"] =round(value_converter((car_data1["Age"])))

# Deine the kilmeter into monthly 
def value_converter(km_val1, km_val2):
    km_convert = km_val1/12
    km_ratio_value = km_val2 / km_val1
    return [km_convert, km_ratio_value]

# add the value into tha km per month column
car_data1["Age Convert"], car_data1["KM per Month"] = \
    value_converter(car_data1["Age"], car_data1["KM"]) 
    
