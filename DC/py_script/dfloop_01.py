import pandas as pd 
brics = pd.read_csv("brics.csv", index_col = 0)

for val in brics:
    print(val)