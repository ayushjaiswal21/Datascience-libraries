import numpy as np #importing module
import randome
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
np.arrange(0,15)
np.linespace(0,20,5)
#generates evenly spaced array between minimum and maximum value given)
np.ones((3,3))
#generated matrix
np.zeros(5)
#generates matrix with zeros
np.eye(2)#it return 2d array
np.randome.randint(3,12)#generated random integer
#"numpy in-built functions"
array1 = np.array([1,2,3,4,5])
np.min(array1)#smallest no.
np.log(array1)#log
np.square(array1)#square
np.mean(array1)#mean value
#copy array
sample = np.array([10,20,30,40,50])
copy_sample = sample.copy()
copy_sample[:]=100
print(copy_sample)

#arithmetic operations on array
sample+copy_sample #for add
sample/copy_sample #for divide
sample*copy_sample #for multiply
sample-copy_sample #for subtract

#remove duplicates
x=np.array([1,2,3,1,4,2,5,3,6,4,1])
np.unique(x)

# transpose ad array
a=np.array([[1,2],[3,4],[5,6]])
a.transpose()

#sorting
m=np.array([[2,1,4],[3,7,4],[8,5,10]])
np.sort(m)

#concatenation
data1 = np.array([[1,2,3],[4,5,6]])
data2= np.array([[11,22,33],[44,55,66]])
np.hstack((data1,data2))
np.vstack((data1,data2))
