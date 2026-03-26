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
