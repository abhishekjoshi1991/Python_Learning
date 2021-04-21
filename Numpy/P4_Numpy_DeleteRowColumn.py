import numpy
'''
syntax: delete(arr, obj, axis=None)
here obj : Indicate indices of sub-arrays to remove along the specified axis

1D array works differently in terms axis designation, there only axis 0 is present
'''
a = numpy.array([1, 2, 3])
newArray = numpy.delete(a, 1, axis=0) #delete first index along column
print(newArray)

a = numpy.array([[1, 2, 3], [4, 5, 6], [10, 20, 30]])
newArray = numpy.delete(a, 0, axis=1) # delete 0th index along row
newArray2 = numpy.delete(a, 1, axis=0)  # delete the 1st index along the column
print(newArray)
print(newArray2)

#liitle confusing