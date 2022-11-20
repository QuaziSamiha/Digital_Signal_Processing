import numpy as np
import matplotlib.pyplot as plt

srate = 256  # sampling rate in Hz
t = np.arange(0., 1., 1/srate)  # time vector in seconds

#  difference between sine and cosinewave is
# 1. phase difference 180 degree
# 2. at the beginning amplitude of cosine is maximum and amplitude of sine is minimum

sineWave = 3 * np.sin(2 * np.pi * 5 * t)
cosineWave = 3 * np.cos(2 * np.pi * 5 * t)

plt.figure(figsize=(10, 6))

plt.plot(t, sineWave, 'y', linewidth=1, label='SineWave')
plt.plot(t, cosineWave, 'r', linewidth=1, label='CosineWave')

plt.xlabel('Time', fontsize=10)
plt.ylabel("Amplitude", fontsize=10)
plt.title("Sine and Cosine waves comparison", fontsize=10)
plt.legend(fontsize=10)
plt.xlim([0, 1])

plt.show()
