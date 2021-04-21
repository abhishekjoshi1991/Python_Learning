#output of some python programs--> from geeks fro geeks


# 1. hint: .upper() does not affects parent string

mylist = ['geeks', 'forgeeks'] 
for i in mylist: 
    i.upper() 
print(mylist)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#2. Hint: loop not terminates as new elements continously added (infinite for loop)
'''
mylist = ['geeks', 'forgeeks'] 
for i in mylist: 
    mylist.append(i.upper()) 
print(mylist)
'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#3. Hint: True and False are keywords and can't be changed

'''
True = False
while True: 
    print(True) 
    break
'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#4. Hint: range() only takes starting value, doesnot change with assignment

a='abhishek'
for i in range(len(a)):
    print(a)
    a='b'

'''in above program range(8) is defined only once, as a becomes
string b that does not mean that value of range will become
range(1)'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#5.
print('\n')
for i in [1, 2, 3, 4][::-1]: 
    print (i)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#6.Hint: loop will break after break statement

L1 = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True] 
val1, val2 = 0, '' 
for x in L1: 
    if(type(x) == int or type(x) == float): 
        val1 += x 
    elif(type(x) == str): 
        val2 += x 
    else: 
        break
print(val1, val2)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#7.
L1 = [1, 2, 3, 4] 
L2 = L1 
L3 = L1.copy() 
L4 = list(L1) 
L1[0] = [5] 
print(L1, L2, L3, L4)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#8. Hint: t1(1) is int and t1(1,) is tuple, comma is important to know its tuple
'''
T1 = (1) 
T2 = (3, 4) 
T1 += 5
print(T1) 
print(T1 + T2) #throws type error
'''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#9. hint: True has value of 1
List = [True, 50, 10]
List.insert(2, 5)    
print(List, "Sum is: ", sum(List))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#10. pop method throws the result and remove method throws nothing at o/p
L = [1, 3, 5, 7, 9]
print(L.pop(-3), end = '  ')
print(L.remove(L[0]), end = '  ')
print(L)
