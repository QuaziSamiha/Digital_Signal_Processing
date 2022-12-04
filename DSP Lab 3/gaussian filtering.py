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

# Generating Gaussian Kernel/Filter..
N = 100
fwhm = 50  # ms # full-width half-maximum
Gtime = 1000*np.arange(-N,N)/srate
Gfilter = np.exp( -(4*np.log(2)*Gtime**2)/fwhm**2  )
Gfilter = Gfilter/np.sum(Gfilter)  # Normalizing the Gaussian Filter.

# Plotting Gaussian Filter.
plt.figure(figsize=(8,5))
plt.plot(Gtime, Gfilter, 'm', linewidth=3, label='Gaussian Filter')

plt.legend(fontsize=10)
plt.show()

# Zero Padding...to avoid edge effect.
sig_4_filter = np.concatenate((np.zeros(N), NoisySignal, np.zeros(N)), axis=0   )
K = len(NoisySignal)
timeindex = np.concatenate( (np.arange(-N,0), np.arange(0,K), np.arange(K,K+N)), axis=0 )
time_4_filter = timeindex/srate

print(len(timeindex))
print(len(sig_4_filter))

# Initialize the filtered signal..
Gfilt_sig = np.zeros(sig_4_filter.shape[0])

# Applying Gaussian Filter...
for i in range(0, NoisySignal.shape[0]):
  Gfilt_sig[i] = np.sum(sig_4_filter[i:2*N+i]*Gfilter)

#Plotting Filtered Signal...
plt.figure(figsize=(10,5))

plt.plot(time_4_filter, sig_4_filter, 'c-', label='Noisy Signal.')
plt.plot(time_4_filter, Gfilt_sig, 'r-', label='Filtered Signal.')

plt.legend(fontsize=10)
plt.show()