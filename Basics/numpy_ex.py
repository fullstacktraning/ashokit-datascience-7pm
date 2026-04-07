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
list1 = np.arange(6)
list2 = list1.reshape(2,3)
print( list2 )