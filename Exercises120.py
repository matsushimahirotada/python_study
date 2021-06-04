import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(1,0.25,10000)
plt.hist(x,bins=20,density=True,rwidth=0.8)