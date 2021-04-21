import numpy
a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[400], [800]])
c= [[33,44,55]]

newArray = numpy.append(a, b, axis=1) #add or append row wise
print(newArray)

newArray = numpy.append(a, c, axis=0) #append column wise
print(newArray)

