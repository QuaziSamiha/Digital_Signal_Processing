import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))

x1 = np.array([1, 2, 2, 1, 1])
n1 = np.array([0, 1, 2, 3, 4])

plt.subplot(2, 2, 1)
makerline, stemlines, baseline = plt.stem(n1, x1, label='x1')
plt.legend(fontsize=10)
plt.setp(stemlines)

x2 = np.array([3, 2, 1])
n2 = np.array([0, 1, 2])

plt.subplot(2, 2, 2)
markerline, stemlines, baseline = plt.stem(n2, x2, label='x2')
plt.legend(fontsize=10)
plt.setp(stemlines)

fliped_x2 = x2[::-1]
n3 = [-2, -1, 0]
plt.subplot(2,2,3)
makerline, stemlines, baseline = plt.stem(n3, fliped_x2, label='Flipped Signal')
plt.setp(stemlines)

plt.show()
