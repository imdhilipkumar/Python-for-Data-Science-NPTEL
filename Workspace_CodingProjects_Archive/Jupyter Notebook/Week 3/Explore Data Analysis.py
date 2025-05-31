import os # for wrking file directory
os.chdir(r"D:\Code-Hero-Hub\PYTHON\Data Science\Spyder")#changing the working directory

# importing the Necesary Modules
import pandas as pd # for Dataframes works
import numpy as np # for the numerical computation

# read the csv files
car_data = pd.read_csv("Toyota.csv")
car_data = pd.read_csv("Toyota.csv", index_col= 0)
car_data = pd.read_csv("Toyota.csv", index_col= 0, na_values=["??", "????"])

# Copy the dataset for Avoid the information loss

car_data1 = car_data.copy()


# Frequency tables
 
freq_table = pd.crosstab(index=car_data1["FuelType"], columns = "Count", dropna= True)

# Two way Table

freq_table = pd.crosstab(index= car_data1["Automatic"], columns = car_data1["FuelType"], dropna = True)

# Two Way - Join Probablity

freq_table = pd.crosstab(index= car_data1["Automatic"], columns = car_data1["FuelType"],normalize=True,  dropna = True)

# Two Way - Marginal Probablity
freq_table = pd.crosstab(index= car_data1["Automatic"], columns = car_data1["FuelType"],normalize=True, margins= True,  dropna = True)
# Two way - Conditional Probalbity
frq_table = pd.crosstab(index= car_data1["Automatic"], columns = car_data1["FuelType"],normalize="index", margins= True,  dropna = True)


# Correlation

numerical_data = car_data1.select_dtypes(exclude =[object])
numerical_data.shape

# corr
corr_data = numerical_data.corr()