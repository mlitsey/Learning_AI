import pandas as pd 
brics = pd.read_csv("brics.csv", index_col = 0)

for lab, row in brics.iterrows():
    brics.loc[lab, "name_length"] = len(row["country"])
print(brics)
    