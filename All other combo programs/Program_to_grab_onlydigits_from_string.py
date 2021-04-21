#Program to grab only digits from a string

string='agdahfkfhsf5ssbghsgfs556dfhgdfhhh98'
for i in string:
    if i.isdigit():
        print(i,end='')
