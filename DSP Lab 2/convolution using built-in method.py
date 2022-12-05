import numpy as np
import matplotlib.pyplot as plt

xn = np.array([1,2,3,1]) # origin at 0
hn = np.array([1,2,1,-1]) # origin at 1

yn = np.convolve(xn, hn, mode='full') 
print(yn) # [ 1  4  8  8  3 -2 -1]
plt.stem(yn)
# find origin
# convolution by loop