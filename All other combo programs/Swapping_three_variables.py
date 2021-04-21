#swapping three variables without using third variable
#c-->a, a-->b, b-->c


a,b,c=10,20,30

a = a + b + c  #a=10+20+30=60
b = a - (b+c) # (b = 60 – (20+30) =10) 
c = a - (b+c) # (c = 60 – (10 + 30) = 20) 
a = a - (b+c) #(a = 60 – (10 + 20) = 30)

print(a,b,c)
