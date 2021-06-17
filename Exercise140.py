import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as norm
import matplotlib.ticker as ticker


def p(N,e):
    n=N
    S=[]
    E=[]
    Ebar = []
    std = 0
    
    while True:
        for i in range(5):
            S=np.random.uniform(-1.0,1.0,100) 
            E.append(sum(S)/n)
            std = np.std(E)
        else:
            if(std<e):
                break
            else:
                n=n*10
                E.clear()
                continue
            
    return E
            
            
N=100.0

e = 10**(-3)
S = [[0]*100]*5
Ebar = []
E=[]
fig = plt.figure()
ax=fig.add_subplot(111,xlim=(-e,e))


for k in range(100):
    E=p(N,e)
    Ebar.append(np.average(E))
    

ax.set_xlabel('x')
ax.set_ylabel('Density')
cs=ax.plot
ax.hist(Ebar,bins=25,rwidth=0.8)

plt.show()
    

