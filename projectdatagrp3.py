<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Data Group 3</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f9f9f9; }
        h1, h2 { color: #333; }
        pre { background: #efefef; padding: 10px; overflow-x: auto; border-radius: 6px; }
    </style>
</head>
<body>
    <h1>Project Data Group 3 Analysis</h1>

    <p><strong>Original File:</strong> <a href="https://colab.research.google.com/drive/1klk5WsxCRHzqc1YWuRf1qoRxpFbvFSol" target="_blank">Colab Link</a></p>
    <p><strong>Dataset URL:</strong> <a href="https://raw.githubusercontent.com/Dinahak/Project-Data/main/Project_data.xlsx" target="_blank">Project_data.xlsx</a></p>

    <h2>Python Code</h2>
    <pre><code># Required Libraries
import pandas as pd
import requests
from io import BytesIO
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load Data
url = 'https://raw.githubusercontent.com/Dinahak/Project-Data/main/Project_data.xlsx'
response = requests.get(url)
project3 = pd.read_excel(BytesIO(response.content))

# Display Head and Info
project3.head()
project3.info()
project3.shape

# Missing Values
missing_info = project3.isnull().sum()
missing_info = missing_info[missing_info > 0]

# Column Review
project3.columns.to_list()

# Descriptive Statistics
project3.describe()

# Happiness Columns Analysis
happiness_columns = [col for col in project3.columns if 'happiness' in col.lower()]

for col in happiness_columns:
    print(f"\nStatistics for: {col}")
    print(f"Mean:   {project3[col].mean()}")
    print(f"Median: {project3[col].median()}")
    print(f"Mode:   {project3[col].mode().tolist()}")

# Gender Based Happiness
for col in happiness_columns:
    grouped = project3.groupby('Gender')[col]
    for gender, data in grouped:
        print(f"\nGender: {gender} - {col}")
        print(f"Mean: {data.mean()}, Median: {data.median()}, Mode: {data.mode().tolist()}")

# Average Happiness by Job
avg_happiness_by_job = project3.groupby('Job_Title')['Happiness_Salary'].mean().reset_index()

# Clean Job Titles
project3['Job_Title'] = project3['Job_Title'].str.replace(r'^Other \(Please Specify\):', '', regex=True).str.strip().str.lower()

# Mapping Similar Job Titles
job_mapping = { 'data engineer':'analytics engineer', 'data analyst': 'data analyst', 'business analyst': 'data analyst', ... }
project3['Job_Title_Clean'] = project3['Job_Title'].str.strip().str.lower()
project3['Grouped_Job_Title'] = project3['Job_Title_Clean'].map(job_mapping).fillna('Other')

# Visualization: Happiness by Job
avg_happiness_table = project3.groupby('Grouped_Job_Title')['Happiness_Salary'].mean().reset_index().sort_values(by='Happiness_Salary', ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(data=avg_happiness_table, x='Happiness_Salary', y='Grouped_Job_Title', palette='pastel')
plt.title('Average Happiness with Salary by Job Title')
plt.xlabel('Average Happiness Salary Rating')
plt.ylabel('Job Title')
plt.tight_layout()
plt.show()

# Work-Life by Country
worklife_by_country = project3.groupby('Country')['Happiness_WorkLife'].mean().reset_index().sort_values(by='Happiness_WorkLife', ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(data=worklife_by_country, x='Happiness_WorkLife', y='Country', palette='Blues_r')
plt.title('Average Work-Life Happiness by Country')
plt.tight_layout()
plt.show()

# Work-Life by Country and Gender
worklife_gender_country = project3.groupby(['Country', 'Gender'])['Happiness_WorkLife'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=worklife_gender_country, x='Happiness_WorkLife', y='Country', hue='Gender', palette='Set2')
plt.title('Work-Life Happiness by Country and Gender')
plt.tight_layout()
plt.show()

# Gender Distribution Pie
gender_counts = project3['Gender'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=90, wedgeprops={'edgecolor': 'black'})
plt.title('Gender Distribution (Pie Chart)')
plt.axis('equal')
plt.show()

# Top Programming Languages
top_languages = project3['Fav_Language'].value_counts().head(3).index.tolist()
filtered_project3 = project3[project3['Fav_Language'].isin(top_languages)]
lang_job_gender = filtered_project3.groupby(['Grouped_Job_Title', 'Fav_Language', 'Gender']).size().reset_index(name='count')

# Grouped Bar Chart for Top Languages
plt.figure(figsize=(14, 7))
sns.barplot(data=lang_job_gender, x='count', y='Grouped_Job_Title', hue='Gender', palette='Set2')
plt.title('Top 3 Programming Languages Across Job Titles (Grouped by Gender)')
plt.tight_layout()
plt.show()

# Boxplot for Salary Happiness by Gender
plt.figure(figsize=(8, 6))
sns.boxplot(data=project3, x='Gender', y='Happiness_Salary', palette='pastel')
plt.title('Distribution of Happiness with Salary by Gender')
plt.tight_layout()
plt.show()
    </code></pre>
</body>
</html>
