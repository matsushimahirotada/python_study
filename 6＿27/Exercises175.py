import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as norm
import matplotlib.ticker as ticker

LHS=[]
RHS=[]
X=[]

a = 0.0
fig = plt.figure()
ax=fig.add_subplot(111,xlim=(0,1.5),ylim=(0,1.2))

while a<=1.5:
    a = a+10**(-2)
    RHS.append(1.0/a)
    X.append(a)
    if a<=1.0:
        LHS.append(1)
    else:
        LHS.append(0)
    

ax.set_xlabel('Threshold')
ax.set_ylabel('Probability')
plt.plot(X,LHS,color="red")
plt.plot(X,RHS)