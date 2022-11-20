import numpy as np
import matplotlib.pyplot as plt

# Constructing a wave with differnt Cosine wave

srate = 256  # sampling rate in Hz
t = np.arange(0., 1., 1/srate)  # time vector in seconds
x1 = 5 * np.cos(2 * np.pi * 2 * t)  # first Cosinewave
x2 = 2 * np.cos(2 * np.pi * 4 * t)  # second Cosinewave
x3 = 7 * np.cos(2 * np.pi * 6 * t)  # third Cosinewave

x4 = x1 + x2 + x3  # combined Cosineewave

# plot every coCosine wave
plt.figure(figsize=(10, 7))
plt.suptitle("Constructing a Wave with Different Cosine Waves")

plt.subplot(2, 2, 1)
plt.plot(t, x1, linewidth=1)
plt.title("CosineWave of amplitude '5' and frequency '2 Hz'", fontsize=10)

plt.subplot(2, 2, 2)
plt.plot(t, x2, linewidth=1)
plt.title("CosineWave of amplitude '2' and frequency '4 Hz'", fontsize=10)

plt.xlabel('time in sec', fontsize=10)
plt.ylabel('Amplitude', fontsize=10)

plt.subplot(2, 2, 3)
plt.plot(t, x3, linewidth=1)
plt.title("CosineWave of amplitude '2' and frequency '6 Hz'", fontsize=10)
plt.xlabel('time in sec', fontsize=10)
plt.ylabel('Amplitude', fontsize=10)

plt.subplot(2, 2, 4)
plt.plot(t, x4, linewidth=1)
plt.title("Combined Cosinewave of above three Cosine wave", fontsize=10)
plt.xlabel('time in sec', fontsize=10)
plt.ylabel('Amplitude', fontsize=10)

plt.show()
