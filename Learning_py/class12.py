#tuple - immutable, same as list, implemented by ()
#tuple unpacking
#traversing
#methods -> has only 2 functions - count, index

tp = (1,20,40,11,56,78)
# tp[1] = 25 --> not allowed

#tuple unpacking

a,b,c = (10,30,50)

a = (30) #unpacking happenig
a = (30,) # now unpacking not happening


#traversing same as list
tp = (10,30,50,50,20,50,20,10)

for elem in tp:
    print(elem)

#tuple methods   - count, index
#count - to get count of values 
print(tp.count(50))

#index - to get index of specific value
print(tp.index(50))