#Program to chech key is in dict, if present print its value

d1={'k1':100,'k2':200,'k3':300,'k4':400}
key=input('enter key to search in dict:')
if key in d1:
    print(d1[key])
else:
    print('key is not present in dict')
