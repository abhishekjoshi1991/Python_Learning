#Program for prime number

'''
logic for program is we have to divide given number by range(2,num),
aswe donot require to divide number by 1 and itself as remainder is zero
in both these cases.

'''

num=int(input('enter the number to check for prime:'))
if num>1:
    for i in range(2,num):
        if num%i==0:
            break
    else:#else must be aligned with for loop
        print('Number is prime number!!')

#============================================================================
#Program to print prime numbers in between given numbers
lower=int(input('enter lower number:'))
upper=int(input('enter upper number:'))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

            
#============================================================================
# Optimized Program to find prime number using function
'''
if we look at concept, for any numbers there won't be such divisor which divides
that number completely after (num/2)

means for number 18, there is no such number after (18/2)=9, that will
divide given number completely

so instead of performing (2,num) iteration we can perform (2,(num//2)+1) iteration
here // is taken to avoid float and +1 is added because for number 4
it will give wrong result as range(2,2) will come and no iteration is performed
in that case
'''

print('\n')
print('optimized program using function')
def prime(num):
    if num>1:
        for i in range(2,(num//2)+1):
            if num%i==0:
                return 'not prime'
        else:
            return 'prime'

print(prime(4))
print(prime(7))
print(prime(40))
