import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(-1, 1,10000)
plt.hist(x,bins=20,density=True,rwidth=0.8)
