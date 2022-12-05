# 11 September, 2022 
#  4 December, 2022
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,2,1,1]) # signal
n = np.array([0,1,2,3,4]) # index

plt.figure(figsize=(6,3))
makerline, stemlines, baseline = plt.stem(n, x, label='discrete signal')
plt.legend(fontsize=10)
plt.show()
