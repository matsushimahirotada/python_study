import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import scipy.stats 
import matplotlib.ticker as ticker

def E(N,e):
    n=N
    S=[]
    E=[]
    ecount=0
    Ebar = []
    std = 0
    
    while True:
        for i in range(5):
            S=stats.norm.rvs(loc=0,scale=0.5,size=n)
            t = 0
            for x in S:
                t=t+np.abs(x)
            E.append(float(t)/float(n))
        else:
            std = np.std(E)
            if(std<e):
                break
            else:
                n=n*10
                E.clear()
                ecount=ecount+1
                continue
                
    return np.average(E)


LHS=[]
RHS=[]
X=[]
E=E(10,10**(-3))

a = 0.0
fig = plt.figure()
ax=fig.add_subplot(111,xlim=(0,1.5),ylim=(0,1.0),xlabel='Threshold',ylabel='Probability')

while a<=1.5:
    a = a+0.1
    X.append(a)
    RHS.append(E/a)
    LHS.append(2*scipy.stats.norm.cdf(-2*a))
    
print(E)

plt.plot(X,LHS,color="red",marker="o",label="LHS")
plt.plot(X,RHS,marker="o",label="RHS")
ax.legend()