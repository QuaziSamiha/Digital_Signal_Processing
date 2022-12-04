# ploting analog signal x(t) = 0.85^t

import numpy as np  # importing class as an object
import matplotlib.pyplot as plt

# Defining analog signal
t = np.arange(0, 11)
x = (0.85)**t
# print(t)
# print(x)

plt.figure(figsize=(6, 5))
plt.suptitle('Analog Signal')
plt.plot(t, x, linewidth=1, label='x(t) = (0.85)^t') # ploting x with respect to t
plt.legend(fontsize=10)
plt.xlabel('time', fontsize=10)  # optional line
plt.ylabel('amplitude', fontsize=10)  # optional line


plt.axis([-0.1, 10.1, 0, 1])  # x_min, x_max, y_min, y_max
plt.rcParams['xtick.labelsize'] = 10
# xticks means values of x
# by default it will increase by 1
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.rcParams['ytick.labelsize'] = 10
# yticks means values of y
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.show()  # draw the above
