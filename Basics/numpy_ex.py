# numpy - numerical python
# numpy operations are speed compared to python lists
# numpy uses less memory compared to python lists
# python lists opeartions are manual and numpy lists are vectorization
# multi-dimensional lists are difficult in python and very eazy in numpy
import numpy as np

# Example - 1
# list1 = np.array([1,2,3,4,5])
# print(list1)

# list2 = np.array([[1,2,3], 
#                   [4,5,6], 
#                   [7,8,9]])
# print(list2)
# print(list2.ndim)
# print(list2.shape)
# print(list2.size)
# print(list2.dtype)

# Example - 2
# print( np.zeros((2,2)) )
# print("-------------------")
# print( np.ones((2,2)) )
# print("-------------------")
# print( np.full((2,2),5) )
# print("-------------------")
# print( np.arange(0,10,2) )
# print("-------------------")
# print( np.linspace(0,1,5) )
# print("-------------------")
# print( np.eye(3) )

# Example - 3 
# list1 = np.array( [10,20,30,40,50] )
# print( list1[0] )
# print( list1[-1] )
# print( list1[0:3] )
# print( list1[1:] )
# print( list1[:2] )
# print( list1[::-1] )

# Example - 4
# list2 = np.array([[1,2,3], 
#                   [4,5,6], 
#                   [7,8,9]])
# print( list2[0,0] )
# print( list2[1,1] )
# print( list2[2,2] )
# print( list2[:,0] )
# print( list2[:,1] )
# print( list2[:,2] )
# print( list2[0,:] )
# print( list2[1,:] )
# print( list2[2,:] )
# print( list2[0:2] )

# Example - 5
# list1 = np.arange(6)
# list2 = list1.reshape(2,3)
# print( list2 )

# Example - 6
# list1 = np.array([1,2,3])
# list2 = np.array([4,5,6])
# print( list1 + list2 )
# print( list1 * list2 )
# print( list1 ** 2 )

# Example - 7
# list = np.array([1,2,3,4,5])
# print( np.mean(list) )          # Average
# print( np.median(list) )        # sort the data, find the middle element
# print( np.sum(list) )           # sum of list elements
# print( np.max(list) )           # max element from list
# print( np.min(list) )           # min element from list
# print( np.std(list) )           # standard deviation

# Example - 8
# list = np.array([[1,2,3],
#                  [4,5,6]])
# print( np.sum(list, axis=0) ) # column-wise sum (axis=0 col)
# print( np.sum(list, axis=1) ) # row-wise sum. (axis=1 row)

# Example - 9
# Broadcasting Example
# list = np.array([10,11,12])
# val = 10
# print( list + val )

# Example - 10
# print( np.random.rand(5) )  # 5 elements will generate & range (0-1)
# print( np.random.randint(1,5) ) # 1 element & range is (1 - 5)
# print( np.random.rand(3,3) ) # 3 X 3 array will create & range (0-1)

# Example - 11
# list = np.array([10,20,30,40,50])
# print( list[list>=30] )

# Example - 12
# list = np.array([3,1,2])
# print( np.sort(list) )
# print( np.where(list > 1) )

# Example - 13
# list1 = np.array([10,20])
# list2 = np.array([30,40])

# list3 = np.concatenate((list1,list2))
# print(list3)

# print( np.split(list3,2) )

# Example - 14
list = np.array([[1,2],
                 [3,4]])
print( np.linalg.inv(list) ) # inverse
print( np.linalg.det(list) ) # det determinant
print( np.linalg.matrix_transpose(list) )