import numpy as np

arr1 = np.arange(10)
print(arr1)

arr2 = np.arange(4, 10)
print(arr2)

arr3 = np.arange(4, 5, 0.2)
print(arr3)

print(np.arange(1, 2, 0.1))


# The arange([start, stop, step, dtype]) : Returns an array with evenly spaced elements as per the interval.

# Parameters : 
# start : [optional] start of interval range. By default start = 0
# stop  : end of interval range
# step  : [optional] step size of interval. By default step size = 1,  
# dtype : type of output array
