import sys
import os
import pandas as pd
 
input_path = sys.argv[1]

df = pd.read_csv(input_path)

df.to_csv("data_raw.csv", index=False)
print("saved raw data")