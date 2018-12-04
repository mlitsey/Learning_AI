import numpy as np 

np.random.seed(123)
outcomes = []

for x in range(10):
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads") # 0: heads
    else:
        outcomes.append("tails") # 1: tails
print(outcomes)