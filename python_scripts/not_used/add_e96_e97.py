import pandas as pd

df = pd.read_csv("input.csv")
    
for row in df.iterrows():
    print(row)
    break

