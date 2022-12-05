import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 10, 100)
frequency = 50
amplitude = 1
theta = np.pi/2
redu = 0.25

# generate reducible complex sine wave

reducible_csw = amplitude * np.exp(redu * time) * np.exp(-1j * (2 * np.pi * frequency * time + theta))

plt.figure(figsize=(10, 5))
plt.plot(time, np.real(reducible_csw), 'b', label='real part')
plt.plot(time, np.imag(reducible_csw), 'm', label='imaginary part')
# plt.xlim(-0.1, 10)
plt.legend(fontsize=10)
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)
plt.show()
