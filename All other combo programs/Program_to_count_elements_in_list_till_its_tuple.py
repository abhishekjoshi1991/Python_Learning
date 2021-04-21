# Count the elements in a list until an element is a Tuple

a=(10,20,30,40,(1,2,3),90)
count=0
for i in a:
    if type(i)!=tuple:
        count+=1
    else:
        break
print(count)
