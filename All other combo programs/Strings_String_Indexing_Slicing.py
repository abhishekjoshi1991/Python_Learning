#Strings

#strings are group of characters
#strings are enclosed in single '' or double "" quotes
#==========================================================================
#printing strings with different quotes
print('abhishek')
print("abhishek")
print('''abhishek''')
print('''abhishek
joshi''')#this allows to print on different lines

#==========================================================================

#String Indexing

name='great python'

'''
+---------------+---+---+---+---+---+---+---+---+---+---+---+---+
|string         | g | r | e | a | t |   | p | y | t | h | o | n |
+---------------+---+---+---+---+---+---+---+---+---+---+---+---+
|index position | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 
+---------------+---+---+---+---+---+---+---+---+---+---+---+---+
|Negative Index |-12|-11|-10| -9| -8|-7 |-6 |-5 |-4 |-3 | -2| -1|
+---------------+---+---+---+---+---+---+---+---+---+---+---+---+

'''
#index out of range error
#print(name[13])

#==========================================================================
#string Slicing

'''
SYNTAX: string[start:stop:step]
+ve step goes in forward direction
-ve step goes in reverse direction
'''

name='great python'
#slicing does not gives index out of range error
print(name[15:180])

#slicing does not print last mentioned index position
print(name[1:5])#it will print from index 1 to index 4 only

#slicing does not print even first character in following case
print(name[9:2]) #it does not print 9th index

#positive step value always goes in forward direction and -ve goes in reverse
print(name[4:])
print(name[4::-1])

#this is important now
print(name[:4:-1])  #it does not gives o/p as taefg
print(name[2:4:-1]) #does not give any o/p

'''so conclusion is, while going in forward direction(2:4) we
can not assign negative step and similarly while going in
reverse direction(10:2) we cannot give positive step value'''

#program to print last 3 characters of string

print(name[9:]) #this will work for only this string
print(name[-3:]) #this will work for any string


#program to print last 3 characters in reverse
print(name[:-4:-1])


#program to print except last 3 characters in forward direction
print(name[:-3])


#program to print except last 3 characters in reverse
print(name[-4::-1])


#program to reverse the string
print(name[::-1])
