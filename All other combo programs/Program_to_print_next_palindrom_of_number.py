#Program to find next palindrom of user defined number

num=int(input('enter the number:'))
while str(num)!=str(num)[::-1]:
    num+=1
else:
    print('Next palindrome:',num)
