# -*- coding: utf-8 -*-
"""ProjectDataGrp3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1klk5WsxCRHzqc1YWuRf1qoRxpFbvFSol
"""

#https://raw.githubusercontent.com/Dinahak/Project-Data/main/Project_data.xlsx

import streamlit as st
import pandas as pd
import requests
from io import BytesIO

url = 'https://raw.githubusercontent.com/Dinahak/Project-Data/main/Project_data.xlsx'

response = requests.get(url)
project3 = pd.read_excel(BytesIO(response.content))

project3.head()

project3.info()

project3.shape

#Identify any remaining columns with missing values and discuss their potential impact on analysis, even if minimal

missing_info = project3.isnull().sum()
missing_info = missing_info[missing_info > 0]  # Filter only columns with missing values
missing_info

#Reviewing column names
project3.columns.to_list()

"""Descriptive Stat

"""

project3.describe()

#Calculate and interpret basic statistics (mean, median, mode) foreach ”Happiness” column

happiness_columns = [col for col in project3.columns if 'happiness' in col.lower()]
happiness_columns

#Calculate mean .median ,mode
# Create a summary table
for col in happiness_columns:
    print(f"\nStatistics for: {col}")
    print(f"Mean:   {project3[col].mean()}")
    print(f"Median: {project3[col].median()}")
    print(f"Mode:   {project3[col].mode().tolist()}")

#statistics separately for male and female groups and compare the results. Are there any notable differences between genders?

# Find columns with "happiness" in the name
happiness_columns = [col for col in project3.columns if 'happiness' in col.lower()]
print("Happiness columns:", happiness_columns)

# Check unique values in the gender column
print("Gender values:", project3['Gender'].unique())

#grouping by Gender
for col in happiness_columns:
    print(f"\n--- Statistics for: {col} ---")

    grouped = project3.groupby('Gender')[col]

    for gender, data in grouped:
        print(f"\nGender: {gender}")
        print(f"  Mean:   {data.mean()}")
        print(f"  Median: {data.median()}")
        print(f"  Mode:   {data.mode().tolist()}")

#Group data by ”Job Title” and find the average ”Happiness Salary”rating per job. Investigate differences between men and women in similar roles

project3.groupby('Job_Title')['Happiness_Salary'].mean().sort_values(ascending=False)

#clean job titles

#Job_Title_cleaned
