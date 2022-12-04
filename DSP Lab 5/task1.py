import numpy as np
import matplotlib.pyplot as plt

# step by step coding for Fourier Transform ( no build in function)

# generating signal
srate = 256  # sampling rate in Hz
t = np.arange(0., 1., 1/srate)  # time vector in seconds
amp = 3
f = 5
x = amp * np.sin(2 * np.pi * f * t) # digital signal

# initializing fourier coefficient
X = np.zeros(len(t), dtype=complex)

for freq in range(0, len(t)):
    # create complex sine wave (csw) or complex component and compute dot product with signal
    csw = np.exp(-1j*2*np.pi*freq*t) # creating complex signal to multiply e^-jw
    X[freq] = np.sum(np.multiply(x, csw)) # ( discrete time signal *  e^jw )


# extract amplitudes
amps = np.abs(X) / len(t) 

# plotting the signal and its fourier transform
plt.figure(figsize=(10,5))
plt.suptitle("signal and its fourier transform", fontsize = 10)

plt.subplot(2, 2 , 1)
plt.plot(t, X, linewidth= 1)
plt.title('Signal of amplitude 3 and frequency of 5 Hz', fontsize = 10)
plt.xlabel('time in sec', fontsize = 10)
plt.ylabel('amplitude', fontsize = 10)

plt.subplot(2, 2 , 2)
markerline, stemlines, baseline = plt.stem(amps)
plt.setp(stemlines, 'linewidth', 3)
plt.title('Fourier transform of a signal', fontsize = 10)
plt.xlabel('Indices', fontsize = 10)
plt.ylabel('Amplitude', fontsize = 10)
