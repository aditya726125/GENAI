'''
variable-- collection of data
function or method-- collection of variable or attribute
class-- collection of variable or attribute and method or function
file-- collection of variable, function and class
module-- collection of file
package-- collection of module
library-- collection of package
numpy -- numerical python - it is used for numerical calculation, data structure of numpy is multidimensional array
'''

import numpy as np
oned_array = np.array([1,2,3])
print(oned_array)

row_vector = np.array([[1,2,3]])
print(row_vector)

column_vector = row_vector.transpose()
print(column_vector)

#operations on row and column vector

#ndim-- dimension
print(oned_array.ndim)
print(row_vector.ndim)

'''
one dimensional array-- [1 2 3]
two dimensional array-- collection of one dimensional array
[[1 2 3]] , [[1 2 3] , [1 2 3]]
'''

print(row_vector.ndim)
print(row_vector.shape)
print(row_vector.size)
print(row_vector.transpose())

rank_one_vector = np.array([1,2,3])
print(rank_one_vector)

twod_array = np.array([[1,2,3],[4,5,6]])
print(twod_array)

#indexing in two dimensional array
print(twod_array[0][1])

#slicing in two dimensional array
print(twod_array[0:2,0:2])

#matrix creation
mat1 = np.matrix("1,2,3;4,5,6;7,8,9")
print(mat1)

#random array
random_array = np.random.random((5,5))
print(random_array)

randint_array = np.random.randint(1,9999, (3,3))
print(randint_array)

data = np.array([1,2,3,4])
power_data = np.power(data,9)
print(power_data)

exp_data = np.exp(data)    #e^x
print(exp_data)

log_data=np.log(data)    #ln(x)
print(log_data)

log2_data=np.log2(data)    #log2(x)
print(log2_data)

log10_data=np.log10(data)    #log10(x)
print(log10_data)

ones_array = np.ones((3,3),dtype = int)
print(ones_array)
