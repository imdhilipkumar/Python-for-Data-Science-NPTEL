# to Change the file Directory
import os
# file Directory Path
os.chdir(r"D:\Code-Hero-Hub\PYTHON\Data Science\Spyder")
# pandas for data frames
import pandas as pd
# Read the dataset a the csv format
Data_csv =pd.read_csv("Iris_data_sample.csv")
Data_csv
# remove the extra column
Data_csv1 = pd.read_csv("Iris_data_sample.csv", index_col=0)
Data_csv1
# Remove the missing value and consider as null
Data_csv2 = pd.read_csv("Iris_data_sample.csv", index_col=0, na_values=["??", "###"])
Data_csv2
# read the Dataset as text file
Data_txt = pd.read_table("Iris_data_sample.txt")
Data_txt
# remove the extra column
Data_txt1 = pd.read_table("Iris_data_sample.txt", index_col=0)
Data_txt1
# Remove the missing value and consider as null
Data_txt2 = pd.read_table("Iris_data_sample.txt", sep=" ")
Data_txt2
# Remove the missing value and consider as null
Data_txt3 = pd.read_table("Iris_data_sample.txt", index_col=0, na_values=["??", "###"], delimiter=" ")
Data_txt3
# Read the Dataset as Excel format
Data_Excel =pd.read_excel("Iris_data_sample.xlsx")
Data_Excel
# remove the extra column
Data_excel1 = pd.read_excel("Iris_data_sample.xlsx", index_col=0)
Data_excel1
# Remove the missing value and consider as null
Data_excel2 = pd.read_excel("Iris_data_sample.xlsx", index_col=0, na_values=["??", "###"])
Data_excel2
