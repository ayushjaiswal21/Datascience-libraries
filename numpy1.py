import numpy as np #importing module
list=[1,2,3,4]
a=np.array(list)
print(type(a))
# this will print type of a that is list . we use numpy so that we can work on arrays in python.
#outut will be = numpy.nd.array
print(a.shape)
lists=[[1,2,3],[4,5,6],[7,8,9]]
b=np.array(lists)
print(b.shape)
#output = (3,3)
b.reshape(3,3)
#convert row into column or vice versa
#now convert into high dimension array 
arr1=np.array([5,6,7,8],ndmin=5)
print(arr1)
#output will be = [[[[[5,6,7,8]]]]]
