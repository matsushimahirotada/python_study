import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as norm
import matplotlib.ticker as ticker
import math 


def p(N,e,t,a,b):
    n=N
    S=[]
    E=[]
    ecount=0
    Ebar = []
    std = 0
    
    while True:
        for i in range(5):
            S=np.random.uniform(a,b,n) 
            sum=0.0
            for x in S:
                sum = sum + math.exp(t*x)
                
            E.append(float(sum)/float(n))
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

a=-1
b=1
t=-2.0
N = 10
X=[]
RHS=[]
LHS=[]

while t <=0:
    e = 10.0**(-3)*(10**t)
    X.append(math.log10(10**t))
    LHS.append(math.log10(p(N,e,10**(t),a,b)))
    temp = ((10**t)*(10**t)*(b-a)*(b-a))/8.0
    RHS.append(math.log10(math.exp(temp)))
    t=t+0.1

fig = plt.figure()
ax=fig.add_subplot(111,xlabel='log10(x)',ylabel='Probability')
plt.plot(X,LHS,color="red",marker="o",label="LHS")
plt.plot(X,RHS,marker="o",label="RHS")
ax.legend()
    