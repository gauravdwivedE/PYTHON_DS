'''
1. Modules and Packages

Modules are just a files in our python (.py)
Packages are the collection of files in our python

'''

from ud_packages import num, str 
from ud_packages.num import sum, multi
from ud_packages.str import find


print(find("hello", "l"))
print(sum(20,40))
print(multi(20,40))
