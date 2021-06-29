import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as norm
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
            S=stats.uniform.rvs(loc=-1,scale=1,size=n)
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
ax=fig.add_subplot(111,xlim=(0,1.5),ylim=(0,1.0))

while a<=1.5:
    a = a+0.1
    X.append(a)
    RHS.append(0.5/a)
    LHS.append(max([0,1-a]))
    
print(E)
ax.set_xlabel('Threshold')
ax.set_ylabel('Probability')
plt.plot(X,LHS,color="red",marker="o")
plt.plot(X,RHS,marker="o")