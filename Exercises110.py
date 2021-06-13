import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as norm

    fig = plt.figure()
    plt = fig.add_subplot(111,xlim = (-1.5,1.5))
    plt.set_xlabel('x')
    plt.set_ylabel('Density')
    
    x=np.random.uniform(-1.0, 1.0,10000)
    X = np.linspace(-1.5, 1.5, 100)
    
    plt.hist(x,bins=20,rwidth=0.8,density=True)
    plt.plot(X, norm.uniform.pdf(X,loc=-1, scale=2), c="red",linewidth = 5.0)