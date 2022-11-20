import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Create a signal...
srate = 256 # Hz
t = np.arange(0,3,1/srate)
pnts = len(t)

x = np.sin(2*np.pi*2*t)
noise = 5*np.random.randn(pnts)
NoisySignal = x+noise

plt.figure(figsize=(10,5))
style.use('dark_background')
plt.plot(t, NoisySignal, 'g', label='Noisy SIgnal')
plt.legend(fontsize=10)
plt.show()

N = 30  # N = Order of moving average filter. Filter window 
# is actually: (2N+1).
# Increasing the order of filter will increase the 
# smoothness of filtered signal.
S_NS = NoisySignal.shape[0]
print(S_NS)
#Initialize denoised signal...
filt_sig = np.zeros(NoisySignal.shape[0])
# Applying moving average filter...

for i in range(0, NoisySignal.shape[0]):
  filt_sig[i] = np.mean(NoisySignal[i:(2*N+1)+i])


plt.figure(figsize=(10,5)) 
style.use('dark_background')

plt.plot(t, NoisySignal, 'g-', label='Noisy Signal')
plt.plot(t, filt_sig, 'r-', linewidth=3, label='Filtered Signal.')

plt.legend(fontsize=15)
plt.show()

