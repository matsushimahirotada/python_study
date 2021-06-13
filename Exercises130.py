import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

num = np.arange(1,4,1)
prob_true = []
prob_empirical = []
count = [0,0,0]
n=100

for i in num:
    value = (i+2)/12
    prob_true.append(value)
    
for i in range(n):
    x = np.random.rand()
    if x<prob_true[0]:
        count[0] = count[0] + 1
    elif prob_true[0] <= x <prob_true[1]+prob_true[0]:
        count[1] = count[1] + 1
    elif prob_true[1] + prob_true[0]<= x < 1.0:
        count[2] = count[2] + 1
    
    
    
dataset = pd.DataFrame([[prob_true[0],count[0]/n],
                         [prob_true[1],count[1]/n],
                         [prob_true[2],count[2]/n]],
                       columns=['Empirical', 'True'], 
                       index=['1', '2', '3'])

        
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(ylabel='Probability')
dataset.T.plot(kind='bar', stacked=True, ax=ax)
plt.show()