import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as norm
import matplotlib.ticker as ticker


def p(N,e):
    n=N
    S=[]
    E=[]
    ecount=0
    Ebar = []
    std = 0
    
    while True:
        for i in range(5):
            S=np.random.uniform(-1.0,1.0,n) 
            t = 0
            for x in S:
                if x<=-0.5:
                    t = t+1
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
    E.append(ecount)
            
    return E
            
            
N=10

e = 10**(-3)
Ebar = []
E=[]
Ex= 0.25
ecount = 0
fig = plt.figure()
ax=fig.add_subplot(111,xlim=(-e,e))


for k in range(100):
    E=p(N,e)
    ecount = ecount + E.pop(-1)
    Ebar.append(np.average(E))
    

ax.set_xlabel('P[x<=-0.5]')
ax.set_ylabel('Density')
cs=ax.plot
ax.hist(Ebar,bins=25,rwidth=0.8)
y_min,y_max=ax.get_ylim()
plt.vlines(Ex+e,0,y_max,colors="red",linestyle="dashed")
plt.vlines(Ex-e,0,y_max,colors="red",linestyle="dashed")
plt.vlines(Ex,0,y_max,colors="red")
plt.xlim(Ex-e*2,Ex+e*2)
plt.grid(True)
print(ecount)

