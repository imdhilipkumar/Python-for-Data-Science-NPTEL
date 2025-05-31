import os 
import pandas as pd
import numpy as np

# Change working directory
os.chdir(r"D:\Code-Hero-Hub\PYTHON\Data Science\Spyder")

# Load dataset
car_data = pd.read_csv("Toyota.csv", index_col=0)
car_data1 = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])
car_data2 = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])

# Check data attributes
print(car_data.info())
print(car_data1.info())

# Convert categorical columns
car_data1["MetColor"] = car_data1["MetColor"].astype("object")
car_data1["Automatic"] = car_data1["Automatic"].astype("object")

# Check memory usage
print(car_data["FuelType"].nbytes)
print(car_data["FuelType"].astype("category").nbytes)

# Replace incorrect values in "Doors"
car_data1["Doors"].replace({"three": 3, "four": 4, "five": 5}, inplace=True)

# Ensure "Doors" column is numeric
car_data1["Doors"] = car_data1["Doors"].astype("int64")

# Final dataset info
print(car_data1.info())

# insert the new column called price class
car_data1.insert(10, "Price class", "")
car_data2.insert(10, "Price class", "")
# using for loop to insert the value in price class & inset the values

for i in range(0, len(car_data1['Price']), 1):
    if (car_data1['Price'][i] <= 8450):
        car_data1['Price class'][i] = "Low"
    elif (car_data1['Price'][i] > 11950):
        car_data1['Price class'][i] = "High"
    else:
        car_data1['Price'][i] = "Medium"

        

# using while to get the data
j = 0
while j<len(car_data2['Price']):
    if car_data2['Price'][i] <= 8450:
        car_data2['Price class'][i] = "Low"
    elif car_data2['Price'][i]>=11950:
        car_data2['Price class'][i] = "High"
    else:
        car_data2['Price'][i] = "Medium"
    j = j+1

# insert in to the column
car_data1['Price class'].value_counts()

    