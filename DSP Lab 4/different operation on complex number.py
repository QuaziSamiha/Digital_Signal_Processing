import numpy as np
import matplotlib.pyplot as plt

z = complex(3,4)
# print(z)

# Extracting Real and Imaginary part of complex number.
print(np.real(z))
print(np.imag(z))

z1 = complex(2,3)
z2 = complex(7,5)
# z3 = complex(2,3)
# z4 = complex(0,5)

# multiplying complex numbers
zm = z1 * z2
print(zm)
## Division of Complex Numbers 
zd = z1/z2
print(zd)

# conjugate of a complex numbet
print(np.conj(z1))

# magnitude square
print(z1 * np.conj(z1)) # 2^2+3^2
print(np.abs(z1)**2)

# Magnitude of a Number
mag_z = np.sqrt( np.real(z)**2 + np.imag(z)**2 )
print(mag_z)

# Angle with positive real axis
ang_z = np.angle(z)
print(ang_z)
print(ang_z * 57.3) # angle in degrees