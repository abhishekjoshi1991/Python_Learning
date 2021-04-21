#Dubugging:
#=========

'''
using pdb we can debug the given code.(pdb is one package)

to start, the file which need to debug, we have to go there using
cmd.

type-->
cd 'path of file' (may be need to press g: after in next line)or
e.g
G:
cd Python Ethans
cd All_Programs
cd Debugging

then call command--python(or 3) -m pdf addition_func.py(or file
name) or we can give absolute path also as
python -m pdb "whole path of .py file"

then pdb prompt is seen in which whole .py can be traversed line
by line

1.run 'help' command to see sll options available like below

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where


2.now cursor is at first line of code, press n or next for next line,

if __name__=='__main__':

again press n to next line
x=input('enter value of a:')

then press n again to enter the value
enter value of a:10

repeat until code is finished

in this way, we can traverse through code line by line

3.but such line by line traverse won't be possible for large code
in such case continue or c is used, which stops only for user input

4.'list' command throws entire code, shows the arrow that where we
are right now

5. let say, we are suspecting that at number 9th line, some error
may be there, then we can set the break point at 9th number line
using "break 9" command. so break point is set at 9 line

now if we check list command again, we can that break as B->

6. at break we can check for x value by typing 'x', y value by
typing 'y', 'where' command to see where we are now, 'whatis x' give
data type of x etc

7. to go in detail at number 9 line, use 'step' command, so it will
go inside --call-- of add(a,b) which is defined in first line.
from there we can use next(n) command again to go line by line,
again we can use 'whatis mysum' etc command, then we will come
to know that mysum is str, so result is wrong.

8. in this way we can set multiple break point, list of such breaks
can be seen using 'break' command

9. to clear/delete break point use 'clear breakpoint id ' means
'clear 1'

10. similaraly we can set break point on importing_file.py which is
calling/importing the addition_func file. so using jump we can
go to that file directly.(see video if required)
'''
