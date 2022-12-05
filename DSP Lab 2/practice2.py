# 11 September, 2022
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

x1 = np.array([1, 2, 2, 1, 1])
n1 = np.array([0, 1, 2, 3, 4])

plt.subplot(2, 2, 1) # 2 row 2 column (1st portion)
markerline, stemlines, baseline = plt.stem(n1, x1, label='x1')
plt.legend(fontsize=15)
plt.setp(stemlines)

# generating and ploting x2
x2 = np.array([3, 2, 1])
n2 = np.array([0, 1, 2])

plt.subplot(2, 2, 2) # 2 row 2 column (2nd portion)
markerline, stemlines, baseline = plt.stem(n2, x2, label='x2')
plt.legend(fontsize=15)
plt.setp(stemlines)

# plotting x1 on position 3
plt.subplot(2, 2, 3)
markerline, stemlines, baseline = plt.stem(n1, x1, label='x1')
plt.setp(stemlines)
plt.legend(fontsize=15)
# plt.show()

# flip/fold x2 and plotting
f_x2 = x2[::-1]
n3 = np.array([-2, -1, 0])
plt.subplot(2, 2, 4)
markerline, stemlines, baseline = plt.stem(n3, f_x2, label='flipped x2')
plt.setp(stemlines)
plt.legend(fontsize=15)

plt.show()