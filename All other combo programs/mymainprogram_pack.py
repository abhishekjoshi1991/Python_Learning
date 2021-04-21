#here we will use files from UserDefinedPackages folder(package)

from UserDefinedPackages import some_main_script #importing from main package
from UserDefinedPackages.SubPackage import my_sub_script#importing from subpackage

print(some_main_script.report_main()) #calling the function from some_main_script module
print(my_sub_script.sub_report())

