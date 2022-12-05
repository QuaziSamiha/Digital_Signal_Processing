import numpy as np
import matplotlib.pyplot as plt

z1 = complex(-7,0)
z2 = complex(3,4)
z3 = complex(0,5)


plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.plot([-10, 10], [0, 0], 'g')
plt.plot([0, 0], [-10, 10], 'g')

plt.plot(np.real(z1), np.imag(z1), 'ro', markersize=10, label='z1')
plt.plot([0,-7], [0,0], 'r')
plt.plot(np.real(z2), np.imag(z2), 'mo', markersize=10, label='z2')
plt.plot([0,3], [0,4], 'c')
plt.plot(np.real(z3), np.imag(z3), 'co', markersize=10, label='z3')

plt.legend(fontsize=10)
plt.show()
