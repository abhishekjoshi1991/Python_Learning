#Program to find parameters for line and cylinder using class:
#*************************************************************

#1. Line
'''
we will pass coordinate 1 and coordinate 2 as tuple
'''

#method-1, using indexing

from math import sqrt
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2=coor2
    
    def distance(self):
        return sqrt((self.coor2[0]-self.coor1[0])**2+(self.coor2[1]-self.coor1[1])**2)
    
    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

print('line output using method 1')
l1=Line((3,2),(8,10))
print(l1.distance())
print(l1.slope())


#method-2, using tuple unpacking


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2=coor2
    
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        
        return sqrt((x2-x1)**2+(y2-y1)**2)
    
    def slope(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        
        return (y2-y1)/(x2-x1)

print('\n')
print('line output using method 2')
l1=Line((3,2),(8,10))
print(l1.distance())
print(l1.slope())


#******************************************************************************

#2. Cylinder

class Cylinder:
    pi=3.142
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        return Cylinder.pi*self.radius*self.radius*self.height
    
    def surface_area(self):
        return 2*Cylinder.pi*self.radius*self.height+(2*Cylinder.pi*self.radius*self.radius)

print('\n')
print('o/p for cylinder class')
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
    
