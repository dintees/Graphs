import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("out.dat")

# print(data)

plt.plot(data[:,0], data[:,1], marker='o')
plt.savefig("plot.png")