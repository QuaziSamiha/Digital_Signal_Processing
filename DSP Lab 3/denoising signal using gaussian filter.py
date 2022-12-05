import numpy as np
import matplotlib.pyplot as plt

# Create a signal...
srate = 256 # Hz sampling rate
t = np.arange(0,3,1/srate)
pnts = len(t) 

x = np.sin(2*np.pi*2*t) # creating a sinusoidal signal
 
noise = 5*np.random.randn(pnts) #creating noise
NoisySignal = x+noise #creating noisy signal 

# Generating Gaussian Kernel/Filter..
N = 100
fwhm = 50  # ms # full-width half-maximum
Gtime = 1000*np.arange(-N,N)/srate
Gfilter = np.exp( -(4*np.log(2)*Gtime**2)/fwhm**2  ) # gaussian filter main function
# gaussian mean filter
Gfilter = Gfilter/np.sum(Gfilter)  # Normalizing the Gaussian Filter.

# Plotting Gaussian Filter.
# plt.figure(figsize=(8,5))
# plt.plot(Gtime, Gfilter, 'm', linewidth=3, label='Gaussian Filter')
# plt.legend(fontsize=10)
# plt.show()

# Zero Padding...to avoid edge effect.
signal_for_filter = np.concatenate((np.zeros(N), NoisySignal, np.zeros(N)), axis=0   )
K = len(NoisySignal)
timeindex = np.concatenate( (np.arange(-N,0), np.arange(0,K), np.arange(K,K+N)), axis=0 )
time_for_filter = timeindex/srate

print(len(timeindex))
print(len(signal_for_filter))

# Initialize the filtered signal..
Gaussian_filtered_signal = np.zeros(signal_for_filter.shape[0])
 
# Applying Gaussian Filter...
for i in range(0, NoisySignal.shape[0]):
  Gaussian_filtered_signal[i] = np.sum(signal_for_filter[i:2*N+i]*Gfilter)

#Plotting Filtered Signal...
plt.figure(figsize=(10,5))

plt.plot(time_for_filter, signal_for_filter, 'c-', label='Noisy Signal.')
plt.plot(time_for_filter, Gaussian_filtered_signal, 'r-', label='Filtered Signal.')

plt.legend(fontsize=10)
plt.show()