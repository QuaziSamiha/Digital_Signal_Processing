import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([1, 2, 3, 1])  # origin at 0
x1_org = 0

x2 = np.array([1, 2, 1, -1])  # origin at 1
x2_org = 1

new_org = x1_org + x2_org

yn = np.convolve(x1, x2, mode='full')
print(yn)  # [ 1  4  8  8  3 -2 -1]
print('new origin : ', new_org)

plt.figure(figsize=(8,5))
x_axis = np.arange(-new_org, (x1.size+x2.size-new_org-1), 1)
markerline, stemlines, baseline = plt.stem(x_axis, yn, label='Convolution Signal')
plt.setp(stemlines)
plt.legend(fontsize=10)

plt.show()
