import numpy as np
import matplotlib.pyplot as plt

# Create a signal...
srate = 256 # Hz sampling rate
t = np.arange(0,3,1/srate)
# Printing all numbers from 1 to 2 in steps of 0.1
# print(np.arange(1, 2, 0.1))
# Output: 
# [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9]
# If you try it with the range() function, you get a TypeError.

x = np.sin(2*np.pi*2*t) # creating a sinusoidal signal or base signal

plt.figure(figsize=(10,5))
# The figure() function in pyplot module of matplotlib library is used to create a new figure.
# figsize(float, float): These parameter are the width, height in inches.

# The plot() function in pyplot module of matplotlib library is used to make a 2D hexagonal binning plot of points x, y.
plt.plot(t, x, 'b', label='Noisy SIgnal')
plt.legend(fontsize=10)

plt.show()
