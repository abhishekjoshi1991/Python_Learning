#Student Management System


d1={}
while True:
    print('++++++++++++++++++++++++++++++')
    print('1. Add student')
    print('2. Search student')
    print('3. Delete student')
    print('4. Exit')
    print('++++++++++++++++++++++++++++++')
    choice=int(input('enter the choice:'))
    if choice==1:
        roll=int(input('enter the roll number:'))
        d1[roll]={}
        d1[roll]['name']=input('enter the name of student:')
        d1[roll]['marks']={}
        d1[roll]['marks']['Maths']=int(input('enter maths marks:'))
        d1[roll]['marks']['Eng']=int(input('enter eng marks:'))
        print('\n')
        print(d1)
        
    elif choice==2:
        roll=int(input('enter roll number for which data to be display:'))
        if roll in d1:
            print('details of',roll,'is:', d1[roll])
        else:
            print('roll number does not exists')
        

    elif choice==3:
        roll=int(input('enter roll number for which data to be deleted:'))
        if roll in d1:
            del(d1[roll])
        else:
            print('roll number does not exists')
        print('\n')
        print(d1)
        
    elif choice==4:
        break

    else:
        print('invalid choice!!')
