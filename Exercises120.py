import numpy as np
import matplotlib.pyplot as plt
import scipy.stats 

fig = plt.figure()
plt = fig.add_subplot(111)
data = np.random.normal(1, 0.5, 10000)
plt.set_xlabel('x')
plt.set_ylabel('Density')
plt.hist(data,bins=30,rwidth=0.8,density=True)
x = np.linspace(-0.5, 3, 10000)
plt.plot(x, scipy.stats.norm.pdf(x,1,0.5), c='r',linewidth = 5.0)