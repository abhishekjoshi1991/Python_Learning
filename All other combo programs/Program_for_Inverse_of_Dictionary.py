#Program of inverse of dictionary
#if d1={1:1,2:4,3:9,4:16} then d2 must be d2={1:1,4:2,9:3,16:4}

d1={1:1,2:4,3:9,4:16}
d2={}
for i in d1:
    d2[d1[i]]=i
print(d2)
