import numpy as np
import matplotlib.pyplot as plt

# Create a signal...
srate = 256 # Hz sampling rate
t = np.arange(0,3,1/srate)
pnts = len(t) 

x = np.sin(2*np.pi*2*t) # creating a sinusoidal signal

# The numpy.random.randn() function creates an array of 
# specified shape and fills it with random values 
noise = 5*np.random.randn(pnts) #creating noise
NoisySignal = x+noise #creating noisy signal

S_NS = NoisySignal.shape[0]
# print(S_NS) # 768 points

N = 30  # N = Order of moving average filter. 
# Filter window is actually: (2N+1).
# Increasing the order of filter will increase the 
# smoothness of filtered signal.

#Initialize denoised signal...
# filt_sig size = NoisySignal size
# creating filt_signal of the same shape of noisySignal with zero value
filt_sig = np.zeros(NoisySignal.shape[0]) 
# Applying moving average filter...

for i in range(0, S_NS):
  filt_sig[i] = np.mean(NoisySignal[i:(2*N+1)+i])

plt.figure(figsize=(10,5))
plt.plot(t, NoisySignal, 'y-', label='Noisy Signal')
plt.plot(t, filt_sig, 'r-', linewidth=3, label='Filtered Signal.')
plt.legend(fontsize=15)
plt.show()
