import numpy as np
import matplotlib.pyplot as plt

# application of convolution ---- denoising signal

# create signal
Srate = 256 # Hz sampling rate
t = np.arange(0, 3, 1/Srate)
pnts = len(t) # 768
# print(pnts)
# print(t)

# Creating a noiseless signal
x = np.sin(2* np.pi * 2 * t)

# Creating a random noise
noise = 5*np.random.randn(pnts) # 768 random values will be generated

# Adding noise to signal
NoisySignal = x + noise
# Plotting noisy signal [Pseudo-continuous]
plt.figure(figsize=(10,6))
# plt.plot(t, NoisySignal, label="Noisy Signal")
plt.stem(t, NoisySignal, label="Noisy Signal")
plt.legend(fontsize=10)
plt.show()
