#Standard Boiler Plate File 2
'''
here in this file let's import file 1

when we import File_1 here, o/p of print(__name__) from File_1 will not be __main__
instead it will be name of that file i.e. File_1.

so whatever line of code inside std. boiler plate condition i.e.
if __name__='__main__': will not be executed here in file_2


so std.boiler plate is used to develope new module or to store any garbage code
that won't be executed when we import that file
'''

import File_1 as f

print(f.dif(10,6))
print(f.l1)
