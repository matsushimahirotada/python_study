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
            Sum = 0
            temp=[]
            for j in S:
                temp.append(j*j)
            E.append(sum(temp)/n)
            std = np.std(E)
        else:
            if(std<e):
                break
            else:
                n=n*10
                E.clear()
                temp.clear()
                ecount=ecount+1
                continue
    E.append(ecount)
    
    return E
            
            
N=10

e = 10**(-3)
Ebar = []
E=[]
ecount = 0
Ex = 1.0/3.0
fig = plt.figure()
ax=fig.add_subplot(111,xlim=(Ex-e,Ex+e))


for k in range(100):
    E=p(N,e)
    ecount = ecount + E.pop(-1)
    Ebar.append(np.average(E))
    

ax.set_xlabel('x')
ax.set_ylabel('Density')
ax.hist(Ebar,bins=50,rwidth=0.8)
y_min,y_max=ax.get_ylim()
plt.vlines(Ex+e,0,y_max,colors="red",linestyle="dashed")
plt.vlines(Ex-e,0,y_max,colors="red",linestyle="dashed")
plt.vlines(Ex,0,y_max,colors="red")
plt.xlim(Ex-2*e,Ex+2*e)
plt.grid(True)
print(ecount)

