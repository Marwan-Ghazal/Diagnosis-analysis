import sys
import os
import pandas as pd
import numpy as np
import subprocess
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold

input_path = sys.argv[1]
df = pd.read_csv(input_path)

#Data cleaning
#removing duplicates task 1
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

numeric_cols = [
    "age", "blood_pressure", "cholesterol", "max_heart_rate",
    "plasma_glucose", "skin_thickness", "insulin", "bmi", "diabetes_pedigree"
]
categorical_cols = ["residence_type", "smoking_status", "exercise_angina","gender","chest_pain_type","hypertension", "heart_disease"]

#removing missing values task 2
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

#replacing missing values in categorical columns with mode task 3
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mode()[0])


# Feature Transformation
#encoding residence_type task 1
encoder = LabelEncoder()
df["residence_type"] = encoder.fit_transform(df["residence_type"])

#encoding smoking_status task 2
encoder = LabelEncoder()
df["smoking_status"] = encoder.fit_transform(df["smoking_status"])

numeric_cols_scale = [
    "blood_pressure", "cholesterol", "max_heart_rate",
    "plasma_glucose", "insulin", "bmi", "diabetes_pedigree", 
]
#scale numerical features task 3
scaler = StandardScaler()
df[numeric_cols_scale] = scaler.fit_transform(df[numeric_cols_scale])


#dimensionality reduction
# removing skin thickness column as it is unrelatable task 1
df = df.drop("skin_thickness", axis=1)

# removing low variance columns task 2
numeric_features = df.columns.tolist()
for col in numeric_features:
    if df[col].var() < 0.01:
        df = df.drop(columns=[col])
        print(f"Removed low variance column: {col}")


#pca task 3
pca = PCA(n_components=5)
df_pca = pca.fit_transform(df[numeric_features])
df_pca = pd.DataFrame(
    df_pca,
    columns=[f"PCA_{i+1}" for i in range(5)],
    index=df.index
)
df = pd.concat([df, df_pca], axis=1)

#Discretization
df["age_group"] = pd.cut(df["age"], bins=[0, 30, 50, 100], labels=[1, 2, 3])


#save data
output_file = "data_preprocessed.csv"
df.to_csv(output_file, index=False)
print(f"Saved data_preprocessed.csv: {df.shape[0]} rows, {df.shape[1]} columns")

# Call downstream scripts
scripts = ["analytics.py", "cluster.py", "visualize.py", "visualizee.py"]
for script in scripts:
    if os.path.exists(script):
        print(f"\n--- Running {script} ---")
        try:
            subprocess.run([sys.executable, script, output_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {script}: {e}")
    else:
        if script != "visualizee.py": # Already checked it might be missing
             print(f"Warning: {script} not found.")