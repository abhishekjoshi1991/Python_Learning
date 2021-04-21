#Loops Assignment Questions

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Program to print maximum number from list
print('max number from list(optimized solution)')
a=[50,6,56,14,55,68,42,305,548,142]
x=0
for i in a:
    if i>x:
        x=i
print(x)
print('\n')

#or
print('this is not optimized solution as we are creating another list of index')
x=0
for i in range(len(a)):
    if a[i]>x:
        x=a[i]
print(x)
print('\n')

'''both of the above solution fails when list contains negative numbers, in such
case till give o/p as zero
so proper solution is, instead of setting x=0, set it to first number from list
'''
a=[-5,-50,-65,-10,-56,-6]
x=a[0]
for i in a[1:]:#it will reduce one iteration
    if i>x:
        x=i
print(x)
print('\n')


#======================================================================

#Program for sum of items in list
print('sum of items in list')
list1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in list1:
    sum+=i
print(sum)
print('\n')

'''
-Input : 

[('G', 'E', 'E', 'K', 'S'), ('G', 'E', 'E', 'K', 'S'), ('G', 'E', 'E', 'K', 'S')]

Output : String --> 'GEEKS GEEKS GEEKS'
'''
l1=[('G', 'E', 'E', 'K', 'S'), ('G', 'E', 'E', 'K', 'S'), ('G', 'E', 'E', 'K', 'S')]
str1=''
for i in l1:
    for j in i:
        str1=str1+j
    str1=str1+' '
print(str1)
print('\n')

#======================================================================

'''for star pattern or number patterns, try to think from
row and column wise by taking i for rows and j for columns
'''

#======================================================================
'''
left aligned right angle triangle pattern
*
**
***
****
*****

'''

n=int(input('no of lines of left aligned right triangle:'))
for i in range(1,n+1):
    print('*'*i)

#======================================================================
'''
right aligned right angle triangle pattern
    *
   **
  ***
 ****
*****

'''

n=int(input('no of lines of right aligned right triangle:'))
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)

#======================================================================
'''
equilateral triangle star pattern
    * 
   * * 
  * * * 
 * * * * 
* * * * *

'''

n=int(input('no of lines of equilateral triangle:'))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i)

#======================================================================
'''
inverted left aligned right angle triangle
*****
****
***
**
*

'''

n=int(input('no of lines of inverted left aligned right a.triangle:'))
for i in range(n,0,-1):
    print('*'*i)

#======================================================================
'''
inverted right aligned right angle triangle
*****
 ****
  ***
   **
    *

'''
n=int(input('no of lines of inverted right aligned right a.triangle:'))
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*i)

#======================================================================
'''
inverted equilateral right angle triangle
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

'''
n=int(input('no of lines of inverted equilateral triangle:'))
for i in range(n,0,-1):
    print(' '*(n-i)+'* '*i)

#======================================================================
'''
up and down equilateral triangle
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    *

'''
n=int(input('no of lines for up down equilateral triangle:'))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i)
for j in range(n-1,0,-1):
    print(' '*(n-j)+'* '*j)

#======================================================================
'''
rhombus star pattern
*****
 *****
  *****
   *****
    *****

'''
n=int(input('enter the sides of rhombus star pattern:'))
for i in range(0,n):
    print(' '*(i)+'*'*n)

#======================================================================
'''
number pattern left aligned r. angled triangle (repeated nums)
1
12
123
1234
12345
'''

n=int(input('no of lines right angled number pattern:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print('')
    
#======================================================================
'''
number pattern inverted right angled triangle (repeated nums)
12345
1234
123
12
1
'''
print('\n')
n=int(input('no of lines for inverted right angled number pattern:'))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print('')

#======================================================================
#number pattern right angled triangle with increment in starting
#num at each line
'''
12345
2345
345
45
5
'''
print('\n')
n=int(input('no of lines for inverted right angled number pattern:'))
for i in range(0,n):
    for j in range(i+1,n+1):
        print(j,end='')
    print('')

#======================================================================
#======================================================================
'''following to program logic is same, but o/p varies with
indentation of num=num+1

1 
2 3 
4 5 6 
7 8 9 10

and

1 
2 2 
3 3 3 
4 4 4 4 
'''

# number pattern right angled triangle (non repated numbers)
print('\n')
n=4 #no of lines to print
num=1 #starting from which num to start
for i in range(1,n+1):
    for j in range(0,i):
        print(num,end=' ')
        num=num+1
    print('')

# number pattern right angled triangle with same nums in each line
print('\n')
n=4 #no of lines to print
num=1 #starting from which num to start
for i in range(1,n+1):
    for j in range(0,i):
        print(num,end=' ')
    num=num+1
    print('')


#======================================================================
#======================================================================
#character pattern
'''
A
BB
CCC
DDDD
'''
num=65
n=int(input('no of lines for character pattern:'))
for i in range(1,n+1):
	print(chr(num)*i)
	num+=1

#======================================================================
# continuous character pattern 
'''
A
BC
DEF
GHIJ
'''
num=65
n=int(input('no of lines of continous character pattern:'))
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(num),end='')
        num=num+1
    print('\n')

#======================================================================

# Program to insert given string before elements of list
''' if list is [1,2,3,4] and string is 'emp' then o/p is
['emp1','emp2','emp3','emp4']
'''
print('\n')
a=[1,2,3,4]
b=[]
for i in range(len(a)):
    b.append('emp'+str(a[i]))
print(b)

#======================================================================
''' Program to find words in a text string whose length is
at most 4 and then print all the substring in that string.

Ex: if a string contains ‘TEST’ then we need to print
‘T’, ‘TE’, ‘TES’, ‘TEST’
'''
print('\n')
a='i am a abhi'
for each in a.split():
    if len(each)==4:
        for i in range(len(each)):
            for j in range(i+1):
                print(each[j],end='')
            print('')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




