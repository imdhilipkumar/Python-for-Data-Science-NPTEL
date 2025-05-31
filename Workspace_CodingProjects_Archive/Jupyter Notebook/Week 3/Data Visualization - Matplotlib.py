# import the necessary libaray
import os  # help to chagne the workng directory

os.chdir(r"D:\Code-Hero-Hub\PYTHON\Data Science\Spyder") # chaging the working directory
import pandas as pd # work with the data frames

import numpy as np # work with numerical operation

import matplotlib.pyplot as plt # work with the data  Visualization

# import the data set
car_data = pd.read_csv("Toyota.csv")
data = pd.read_csv("Toyota.csv")

#Find out the null values and remove the extra column
data = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])

# Remove the null values
data.dropna(axis = 0, inplace = True)

# Scatter plot
plt.figure()
plt.scatter((data["Age"]), data["Price"], c ="Green")
plt.title("Scatter Plot of Age & Price")
plt.xlabel("Age")
plt.ylabel("Price")
plt.show()

# Histogram
plt.figure()
plt.hist(data["KM"], color = "Green", edgecolor = "White", bins = 5)
plt.title("Histogram representation of KM")
plt.xlabel("Kilograms")
plt.ylabel("Frequency")
plt.show()

#Bar Plot
counts = [979, 120, 12]
fuelTypes = ("Petrol", "Diesel", "CNG")
index = np.arange(len(fuelTypes))
plt.figure()
plt.bar(index, counts, color = ["green", "Red", "Cyan"])
plt.title("Bar plot for Fuel Types")
plt.xlabel("Fuel Types")
plt.ylabel("Frequency")
plt.xticks(index, fuelTypes, rotation = 90)
plt.show()
