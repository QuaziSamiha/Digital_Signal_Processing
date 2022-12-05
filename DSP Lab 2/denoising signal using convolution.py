import numpy as np
import matplotlib.pyplot as plt

# application of convolution ---- denoising signal

# create signal
Srate = 256 # Hz sampling rate
t = np.arange(0, 3, 1/Srate)
pnts = len(t) # 768

# Creating a noiseless signal
x = np.sin(2* np.pi * 2 * t)

# Creating a random noise
noise = 5*np.random.randn(pnts) # 768 random values will be generated

# Adding noise to signal
NoisySignal = x + noise

# Plotting noisy signal [Pseudo-continuous]
# plt.figure(figsize=(10,6))
# plt.plot(t, NoisySignal, label="Noisy Signal")
# plt.legend(fontsize=10)

# Selecting Filters for Denoising...
filter = 2 * np.ones(50)/10.0 # moving average filter
# print(filter)
# filtering by convolution
# filteredSignal = np.convolve(NoisySignal, filter, mode='full')
filteredSignal = np.convolve(NoisySignal, filter, mode='same')

# Plotting filtered Signal
plt.figure(figsize=(10,6))
# plt.plot(filteredSignal, label='Filtered Signal')
plt.stem(filteredSignal, label='Filtered Signal')
plt.legend(fontsize=10)

plt.show()
