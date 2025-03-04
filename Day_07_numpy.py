#1
'''
Numpy array of shape (3, 4) and assign random integers between 1 and 10 to every element.
'''
import numpy as np

arr = np.random.randint(1,11, size = (3,4))
print(arr)


#2
'''
Maximum value in the array created in step 1.
'''
import numpy as np

# Assuming the array from the previous steps is stored in the variable 'arr'
maxm_value = np.max(arr)
print(maxm_value)


#3
'''
Calculating the mean value of each row in the array.
'''
import numpy as np
# Assuming the array from the previous steps is stored in the variable 'arr'
row_mean = np.mean(arr, axis = 1 )
print(row_mean)


#4
'''
Reshape the array from step 1 into a shape of (2, 6).
'''
import numpy as np

# Assuming the array from the previous steps is stored in the variable 'arr'
reshaped_arr = np.reshape(arr ,(2,6))
print(reshaped_arr)


#5
'''
Multiply each element in the array by 2.
'''
import numpy as np
# Assuming the array from the previous steps is stored in the variable 'arr'
arr = arr*2
print(arr)


#6
'''
Creating a numpy array with values ranging from 0 to 9. Extracting the odd numbers from the array.
'''
import numpy as np

arr = np.arange(10)
odd_number = arr[arr%2!=0]
print(odd_number)


#7
'''
Creating a 3x3 identity matrix using numpy.
'''
import numpy as np

identity_matrix = np.identity(3)
print(identity_matrix)


#8
'''
Creating a 5x5 array with random values and normalize it 
(subtract the mean and divide by the standard deviation of the array). 
'''
import numpy as np

arr = np.random.rand(5,5)
# Calculating the mean and standard deviation
mean = np.mean(arr)
std = np.std(arr)
#normalized_arr = (arr - mean) / std
normalized_arr = (arr - mean) / std
print(normalized_arr)


#9
'''
Performing element-wise multiplication between two arrays of the same shape.
'''
import numpy as np

arr1 = np.array([[1,2,3],
                [4,5,6]])
arr2 = np.array([[2,3,4],
                 [5,6,7]])
#element wise multiplication
result = arr1 * arr2
print(result)


#10
'''
Given an array of heights in centimeters, convert them to inches (1 inch = 2.54 cm).
'''
import numpy as np

heights_cm = np.array([160, 170, 180, 190])
heights_inch = heights_cm / 2.54
print(heights_inch)


#11
'''
Creating a 1D array of numbers from 0 to 9. Replace all odd numbers with -1.
'''

import numpy as np
arr = np.arange(10)
#replacing odd numbers with -1
arr[arr % 2 != 0 ]= -1
print(arr)


#12
'''
Creating a 2D array with random values and finding the indices of the maximum and minimum values.
'''
import numpy as np

arr = np.random.randn(2,3)  # 2x3 matrix with random values
# Find the indices of the maximum and minimum values
max_index = np.unravel_index(np.argmax(arr), arr.shape)
min_index = np.unravel_index(np.argmin(arr), arr.shape)

print("Array:")
print(arr)
print("Maximum value index:", max_index)
print("Minimum value index:", min_index)
