import numpy as np
data=np.loadtxt('Employee.csv',delimiter=',', skiprows=1,
                usecols=(2,3),dtype=float)
print(data)
print(type(data))


#delimiter tag is useful otherwise whole csv will get considered as unstructured data