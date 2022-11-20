import numpy as np
import matplotlib.pyplot as plt

x_sample = np.array([0, 0, 1, 0, 0])
index = np.array([-2, -1, 0, 1, 2])
plt.figure(figsize=(10,5))

# plt.subplot(1, 2, 1) 
markerline, stemlines, baseline = plt.stem(index, x_sample, label='unit sample sequence')
plt.setp(stemlines)
plt.legend(fontsize=15)
plt.show()

flipped_x_sample = x_sample[::-1]
# plt.subplot(1, 2, 1)
markerline, stemlines, baseline = plt.stem(index, flipped_x_sample, label='flipped unit sample sequence')
plt.setp(stemlines)
plt.legend(fontsize=15)

plt.show()

index_shift = np.array([-1,0,1,2,3])
markerline, stemlines, baseline = plt.stem(index_shift, x_sample, label='shifted unit sample sequence')
plt.setp(stemlines)
plt.legend(fontsize=15)
plt.show()
