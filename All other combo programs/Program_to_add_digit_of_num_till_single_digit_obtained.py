'''program to add the digits of a positive integer
repeatedly until the result has a single digit.
For example given number is 59, the result will be 5.
Step 1: 5 + 9 = 14
Step 1: 1 + 4 = 5


In for and while loop, else block of code is executed only when all
iteration of loops are completed and will not get executed when loop
is terminated by break statement or exception is occur.

'''

num=int(input('enter the number:'))
while len(str(num))>1:
    sum=0
    for i in str(num):
        sum=sum+int(i)
    else:
        num=sum
else:
    print(sum)
