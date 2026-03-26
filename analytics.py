import sys
import os
import pandas as pd

input_path = sys.argv[1]

df_raw = pd.read_csv("data_raw.csv")
df = pd.read_csv(input_path)

duplicates_removed = df_raw.duplicated().sum()
total_nulls = df_raw.isnull().sum().sum()

# insight 1
insight1 = "Data Cleaning Overview \n"
 
insight1 += f"Duplicates removed: {duplicates_removed}\n"
insight1 += f"Total null handled: {total_nulls}\n"
 
insight1 += "raw data (first 5 rows)\n"
insight1 += df_raw.head().to_string() + "\n\n"
 
insight1 += "preprocessed data (first 5 rows)\n"
insight1 += df.head().to_string() + "\n"
 
with open("insight1.txt", "w") as f:
    f.write(insight1)

# Insight 2
insight2 = "Data Analysis\n\n"

insight2 += "1. Heart Disease Comparison\n"

with_hd = df[df["heart_disease"] == 1]
without_hd = df[df["heart_disease"] == 0]

insight2 += "Average age:\n"
insight2 += f"With heart disease: {with_hd['age'].mean():.2f}\n"
insight2 += f"Without heart disease: {without_hd['age'].mean():.2f}\n\n"

insight2 += "Average blood pressure:\n"
insight2 += f"With heart disease: {with_hd['blood_pressure'].mean():.2f}\n"
insight2 += f"Without heart disease: {without_hd['blood_pressure'].mean():.2f}\n\n"

insight2 += "Average cholesterol:\n"
insight2 += f"With heart disease: {with_hd['cholesterol'].mean():.2f}\n"
insight2 += f"Without heart disease: {without_hd['cholesterol'].mean():.2f}\n\n"

insight2 += "2. Smoking Status vs Hypertension\n"

smoking_groups = df["smoking_status"].dropna().unique()

for status in smoking_groups:
    group = df[df["smoking_status"] == status]
    percent = (group["hypertension"].sum() / len(group)) * 100
    insight2 += f"{status}: {percent:.1f}% have hypertension\n"

insight2 += "\n"

with open("insight2.txt", "w") as f:
    f.write(insight2)

