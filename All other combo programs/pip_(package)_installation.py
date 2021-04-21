#pip installation

'''
in cmd, if by typing pip, if it is howing that pip is not recognized as internal
or external command then we have to do following procedure

1. go to this pc properties
2. go to advance system setting --> environment variables
3. double click on path
4. by default we have already set python interpreter path as
'C:\Users\Abhishek Joshi\AppData\Local\Programs\Python\Python37'
5. just copy that path and create new path with name as
'C:\Users\Abhishek Joshi\AppData\Local\Programs\Python\Python37\scripts'
6. click on ok
7. environment path gets set



pip list or pip3 list command to see all packages instaaled on system as per the
version of python installed


to unistall any existing package:
pip uninstall 'name of package'
e.g. pip uninstall numpy


while installing package, it goes to pypi.org and install it from their

use coomand --> pip install matplotlib
(matplotlib requires another packages to be first installed on machine to work
,such dependency is also taken care automatically, we do not need to install
those packages first)

#try unistalling and installing matplotlib from pip3

if installation does not start with pip install numpy(say) or pip3 install numpy,
then we can use command "python -m pip install numpy"
this will give control to python scripts to download the package we want to install.

#to install older version of any package use
pip3 install xlrd==1.0.0(version number)

#to upgrade the package , instead of ininstalling older version and then installing
latest version, we can use follwing command to upgrade the package
pip3 install --upgrade xlrd


#to get summary of package
pip3 show xlrd

#for offline installtion of package
-download the tar.gz file of package then in cmd give path of that tar.gz file
like pip3 install 'that file path'


