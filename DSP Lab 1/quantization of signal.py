# sampling and ploting signal x(t) = 0.85^t

import numpy as np  
import matplotlib.pyplot as plt

# Defining analog signal
t = np.arange(0, 11)
x = (0.85)**t

# define sampling rate
n=t
# for quantization
xq = np.around(x, 1) # round function 

plt.suptitle('Quantization of Signal')
# plt.figure(figsize=(6, 5))
plt.plot(t, x, linewidth=1, label='x(t) = (0.85)^t') # plotting x with respect to t
plt.legend(fontsize=10)
plt.xlabel('t', fontsize=10)  # optional line
plt.ylabel('amplitude', fontsize=10)  # optional line

plt.axis([-0.1, 10.1, 0, 1])  # x_min, x_max, y_min, y_max
plt.rcParams['xtick.labelsize'] = 10
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # xticks means values of x
plt.rcParams['ytick.labelsize'] = 10
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) # yticks means values of y

markerline, stemlines, baseline = plt.stem(n, xq)
plt.setp(stemlines, 'linewidth', 1)

plt.axhline(y=0.1, xmin=0, xmax=10, color='r', linewidth=1.0) 
plt.axhline(y=0.2, xmin=0, xmax=10, color='r', linewidth=1.0)
plt.axhline(y=0.3, xmin=0, xmax=10, color='r', linewidth=1.0)
plt.axhline(y=0.4, xmin=0, xmax=10, color='g', linewidth=1.0)
plt.axhline(y=0.5, xmin=0, xmax=10, color='r', linewidth=1.0)
plt.axhline(y=0.6, xmin=0, xmax=10, color='r', linewidth=1.0)
plt.axhline(y=0.7, xmin=0, xmax=10, color='r', linewidth=1.0)
plt.axhline(y=0.8, xmin=0, xmax=10, color='r', linewidth=1.0)
plt.axhline(y=0.9, xmin=0, xmax=10, color='r', linewidth=1.0)
plt.axhline(y=1.0, xmin=0, xmax=10, color='r', linewidth=1.0)

plt.show()  # draw the above
