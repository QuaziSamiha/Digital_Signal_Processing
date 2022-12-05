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
plt.figure(figsize=(8,5))
plt.plot(Gtime, Gfilter, 'm', linewidth=3, label='Gaussian Filter')
plt.legend(fontsize=10)
plt.show()