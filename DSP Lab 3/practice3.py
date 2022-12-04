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
pnts = len(t) #The len() function returns the number of items in an object.

x = np.sin(2*np.pi*2*t) # creating a sinusoidal signal

# The numpy.random.randn() function creates an array of 
# specified shape and fills it with random values 
noise = 5*np.random.randn(pnts) #creating noise
NoisySignal = x+noise #creating noisy signal

S_NS = NoisySignal.shape[0]
# print(S_NS)

N = 30  # N = Order of moving average filter. Filter window 
# is actually: (2N+1).
# Increasing the order of filter will increase the 
# smoothness of filtered signal.

#Initialize denoised signal...
filt_sig = np.zeros(NoisySignal.shape[0])
# Applying moving average filter...

for i in range(0, S_NS):
  filt_sig[i] = np.mean(NoisySignal[i:(2*N+1)+i])


# The figure() function in pyplot module of matplotlib library is used to create a new figure.
# figsize(float, float): These parameter are the width, height in inches.
plt.figure(figsize=(10,5))
# The plot() function in pyplot module of matplotlib library is used to make a 2D hexagonal binning plot of points x, y.
plt.plot(t, NoisySignal, 'y-', label='Noisy Signal')
plt.plot(t, filt_sig, 'r-', linewidth=3, label='Filtered Signal.')
plt.legend(fontsize=15)
plt.show()
