# 21 November, 2022
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# correcting the amplitude and converting frequencies 
srate = 256
t = np.arange(0., 1., 1/srate)
amp = 3
f = 5
x = amp * np.sin(2 * np.pi * f * t) # digital signal

# initializing fourier coefficient
X = np.zeros(len(t), dtype=complex)

for freq in range(0, len(t)):
    # create complex sine wave (csw) or complex component and compute dot product with signal
    csw = np.exp(-1j*2*np.pi*freq*t) # creating complex signal to multiply e^-jw
    X[freq] = np.sum(np.multiply(x, csw)) # ( discrete time signal *  e^jw )

# in this above line of code we multiply by 2 to incorporete negative frequencies
# of complex sinusoidal
# converting indices to frequency
# there are 0 to 256 indices at which we generate the sine wave
# there are frequency indices
# not the frequency in hertz, since we have n = 128 indices including zero
#  therefore after (n/2)
# i. e 128 in
# this case we got the negative waveform of the first 1258 samples , it means after n = 128
# the frequencies ar  the Nyquist criteria
# thus is order to convert indices nto hertz we need (n/2+1) or (n/2) linearly spaced
# samples between zero and
# Nyquist (srate / 2) as shown below

import math
Nyquist = srate/2
Hz = np.linspace(0, Nyquist, math.floor(len(t)/2 + 1))

#  ploting the signal and its fourier transform

plt.figure(figsize = (24, 12))
plt.suptitle('Signal and its fourier transform', fontsize = 25)
style.use('dark_background')

plt.subplot(2,2,1)
plt.plot(t, x, linewidth = 1)
plt.title("signal of amplitude '3' and frequency '5' Hz", fontsize = 15)
plt.xlabel('time in sec', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)

# extract amplitudes
amps = np.abs(X) / len(t) 

plt.subplot(2,2,2)
markerline, stemlines, baseline=plt.stem(Hz, amps[range(0, len(Hz))])
plt.setp(stemlines, 'linewidth', 3)
plt.xlim(0,10)
plt.ylim(0,5)
plt.title('fourier transform of a signal', fontsize=15)
plt.xlabel('frequency in Hz', fontsize = 15)
plt.ylabel('amplitude', fontsize = 15)
plt.show()

srate = 256  # sampling rate in Hz
t = np.arange(0., 1., 1/srate)  # time vector in seconds
amp = 3
x1 = 5 * np.sin(2 * np.pi * 2 * t)  # first Cosinewave
x2 = 2 * np.cos(2 * np.pi * 4 * t)  # second Cosinewave

DC = 2
x3 = DC + x1 + x2   # Sum of sine , cosine and dc
# initializing fourier coefficient
X = np.zeros(len(t), dtype=complex)

for freq in range(0, len(t)):
    # create complex sine wave (csw) or complex component and compute dot product with signal
    csw = np.exp(-1j*2*np.pi*freq*t) # creating complex signal to multiply e^-jw
    X[freq] = np.sum(np.multiply(x3, csw)) # ( discrete time signal *  e^jw )


# extract amplitudes
amps = np.abs(X) / len(t) 

import math
Nyquist = srate/2
Hz = np.linspace(0, Nyquist, math.floor(len(t)/2 + 1))

# plotting the signal and its fourier transform
plt.figure(figsize=(10,5))
plt.suptitle("signal and its fourier transform", fontsize = 10)

plt.subplot(2, 2 , 1)
plt.plot(t, x3, linewidth= 1)
plt.title('Signal of amplitude 3 and frequency of 5 Hz', fontsize = 10)
plt.xlabel('time in sec', fontsize = 10)
plt.ylabel('amplitude', fontsize = 10)
plt.subplot(2,2,2)
markerline, stemlines, baseline=plt.stem(Hz, amps[range(0, len(Hz))])
plt.setp(stemlines, 'linewidth', 3)
plt.xlim(0,10)
plt.ylim(0,5)
plt.title('fourier transform of a signal', fontsize=15)
plt.xlabel('frequency in Hz', fontsize = 15)
plt.ylabel('amplitude', fontsize = 15)
plt.show()

# discrete time periodic signal 
x = [2, -2, 1] 
N = np.arange(0,3,1)
print(N)
#initialize fourier coefficients
coef = np.zeros(len(x),dtype=complex)  # first assign zeros in this array then we will get 3 frequencies 

for n in range(0,3):
  for k in range(0,3):
    #create complex sine wave and compute dot  product with signal 
    csw = np.exp(-1j*2*np.pi*k*n/3)
    coef[n] = (1/3)*np.sum(np.multiply(x[n],csw))  # X =fourier coefficient and freq = index ; ck = summation of x* e^-2*pi*f*t 
  print("C",n," : ",coef[n],sep='')

#finding magnitudes
magnitude=[0,0,0]
import math

temp=0
for i in range (0,3,1):
  temp=np.imag(coef[i])**2
  temp+=np.real(coef[i])**2
  magnitude[i]=math.sqrt(temp)
  print("Magnitude of C",i," : ",magnitude[i],sep='')

#energy density spectra for each of the coefficients
Sxx=[0,0,0]
for i in range (0,3,1):
  Sxx[i]=magnitude[i]**2
  print("Energy density spectra of C",i," : ",sep='',end='')
  print(Sxx[i])

#plotting the signal and it's fourier transform 
plt.figure(figsize=(12,5)) #set 
plt.suptitle('signal and its fourier transform', fontsize=12)

plt.subplot(1,2,1)
plt.plot(N,x)
plt.title("signal of period 3",fontsize=12)
plt.xlabel("time in sec",fontsize=10)
plt.ylabel('amplitude',fontsize=10)

plt.subplot(1,2,2)
plt.plot(N,Sxx)
plt.title("Fourier transform of a signal",fontsize=12)
plt.xlabel('frequency',fontsize=10)
plt.ylabel('energy spectrum',fontsize=10)

plt.show()