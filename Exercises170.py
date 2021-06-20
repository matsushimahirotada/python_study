def p(N,e,P):
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
                if x<=P:
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
                
    return E
            
            
N=10

e = 10**(-3)
Ebar = []
E=[]
X=[]
Ex= 0.75
i = -1.5
ecount = 0
fig = plt.figure()
ax=fig.add_subplot(111,xlim=(-e,e))


while i<=1.5:
    E=p(N,e,i)
    Ebar.append(np.average(E))
    X.append(i)
    i = i+0.1
    

ax.set_xlabel('Threshold')
ax.set_ylabel('Probability')
plt.plot(X,Ebar,marker="o")
y_min,y_max=ax.get_ylim()
plt.xlim(min(X),max(X))
plt.grid(True)