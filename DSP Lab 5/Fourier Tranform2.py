import numpy as np
import matplotlib.pyplot as plt

# step by step coding for Fourier Transform ( no build in function)

# generating signal
srate = 256  # sampling rate in Hz
t = np.arange(0., 1., 1/srate)  # time vector in seconds
amp = 3
f = 5
x = amp * np.size(2 * np.pi * f * t) # digital signal

# initializing fourier coefficient
X = np.zeros(len(t), dtype=complex)

for freq in range(0, len(t)):
    # create complex sine wave (csw) or complex component and compute dot product with signal
    csw = np.exp(-1j*2*np.pi*freq*t) # creating complex signal to multiply e^-jw
    X[freq] = np.sum(np.multiply(x, csw)) # ( discrete time signal *  e^jw )


# extract amplitudes
amps = np.abs(X) / len(t) 

print(amps.shape)
print(amps[22])
print(t.shape)
print(t)

# plotting signal and complex sine wave
plt.figure(figsize=(10, 5))
plt.plot(t, x, linewidth=1, label="Signal with amp = 3 and frequency = 5 Hz")
#  real part means cosine part
plt.plot(t, 3*np.real(csw), 'r-', linewidth=1, label='real part of csw')
# imag part has phase difference
plt.plot(t, 3*np.imag(csw), 'm-', linewidth=1, label='imag part of csw')
plt.xlabel('time', fontsize=10)
plt.ylabel('amplitude', fontsize=10)
plt.title("signal Modelling with complex sine wave", fontsize=10)
plt.xlim([0, 1])
plt.legend(fontsize=10)
plt.show()
