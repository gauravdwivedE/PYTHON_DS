'''
Set 
 -Set can only store hashable values inside set
  we have a hash function this function converts values to hash
  those value that can be converted only can get stored in set 

unoreder - does not follow any oreder because it stores vales accourding to has table in memory
so that it has no indexing support
no duplicate values are allowed

set functions
'''

set = {10,20,40,30,20,60,10}
print(set)

#traversing 
for elem in set:
    print(elem)

for elem in enumerate(set):
    print(elem)

#set functions

set = {10,30,20,40,50}
set2 = {10,30,70,90,100}

print(set.union(set2)) #unique value
print(set.intersection(set2)) #similar values
print(set.difference(set2)) # removes similar values from set 1 and gives it
set.discard(10) #removes 10 from set one and returns none
print(set)
