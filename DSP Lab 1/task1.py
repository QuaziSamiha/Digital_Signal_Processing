from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

t = np.arange(0, 11)
# print(t)
x = (0.85)**t

plt.figure(figsize=(5,6))
plt.suptitle("Analog Signal")
# style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

plt.plot(t, x, linewidth=2, label='x(t) = (085)^t')
plt.legend(fontsize=15)

plt.xlabel('t', fontsize=10)
plt.ylabel('amplitude', fontsize=10)

# Setting the x-axis to -0.1 to 10 and y-axis to 0 to 1
plt.axis([-0.1, 10.1, 0, 1])
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.yticks([0.0,0.1,0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])

plt.show()
