import sys
import os
import pandas as pd
import subprocess

input_path = sys.argv[1]

df = pd.read_csv(input_path)

output_file = "data_raw.csv"
df.to_csv(output_file, index=False)
print(f"saved raw data to {output_file}")

# Call preprocess.py
print("\n--- Running Preprocessing ---")
subprocess.run([sys.executable, "preprocess.py", output_file], check=True)