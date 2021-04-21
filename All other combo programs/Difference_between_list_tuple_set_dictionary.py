#difference between tuple, list, set

#see the classroom video 4, from 13:00 for memory implementation pt of view

'''
list is mutable and tuple is immutable
tuple is faster than list
tuple is lightweight
'''
#---------------------------------------------------------------------------
#set can not be indexed
#s1={1,23,4,5}
#s1[0]--> is not possible, error not subscriptable
#set is immutable, beacuse it is not indexed at all

#---------------------------------------------------------------------------

#dictionary has identifier called as 'Keys' (same as index position of list)
#to fetch values
#dictionary can be indexed based on keys
#dictionary values are mutable and not keys
#dictionary is unordered structure
#dictionary have uniques keys, if we assign two keys with same name then,
#it will fetch recent one
d1={'ID':101,'Name':'Abhi','ID':109}
print(d1['ID'])

#for dictionary keys are taken as immutable objects like int,float,str,tuple
d1={(1,2):(10,20),100:'ABHI','id':'mech'}#this is possible

#on this we can do following operations
print(d1[(1,2)])
print(d1[(1,2)][0])

#but this is not possible form of dict
#d1={[1,2]:[10,20],100:'ABHI','id':'mech'}-->list taken as key instead of tuple

#but we can take list for values
#d1={10:['a','b','c']}


#let
#l1=[101,'abhishek','IT']
#d1={'id':101,'name':'abhishek','dept':'IT'}
#if i want to add salary to list and dict, then

#l1[3]=10000--> is not possible, list index out of range error
d1['salary']=10000 #-- > is possible, check for salary key, if present update else add
