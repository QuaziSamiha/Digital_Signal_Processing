import numpy as np
import matplotlib.pyplot as plt

# Constructing a wave with sine , cosine and dc

srate = 256  # sampling rate in Hz
t = np.arange(0., 1., 1/srate)  # time vector in seconds
x1 = 5 * np.sin(2 * np.pi * 2 * t)  # first Cosinewave
x2 = 2 * np.cos(2 * np.pi * 4 * t)  # second Cosinewave

# what is DC
DC = 2
#  it will be shifted 2 unit in y axis for summing dc
x3 = + DC + x1 + x2   # Sum of sine , cosine and dc

plt.figure(figsize=(20, 4))
plt.suptitle("Constructing a Wave with Sine, Cosine and DC")

plt.subplot(1, 3, 1)
plt.plot(t, x1, linewidth=1)
plt.title("CosineWave of amplitude '5' and frequency '2 Hz'", fontsize=10)


plt.xlabel('time in sec', fontsize=10)
plt.ylabel('Amplitude', fontsize=10)

plt.subplot(1, 3, 2)
plt.plot(t, x2, linewidth=1)
plt.title("CosineWave of amplitude '2' and frequency '4 Hz'", fontsize=10)

plt.subplot(1, 3, 3)
plt.plot(t, x3, linewidth=1)
plt.title("Combine Sine , Cosine and DC", fontsize=10)

plt.show()
