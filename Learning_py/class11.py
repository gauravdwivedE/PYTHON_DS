'''
Hetrogenous - you can strore anything in these type of data structure. eg - 10.5, 10, 'hello'
Homogenous - you can store one type of value
Reference copy
Shallow copy
List traversing 
List method
'''

#homogenous (string)
str = "gaurav"

#hetrogenous (list)
list = [1,"heelo", 10.5, 'k', 33444, 1234567]

#list indexing (same as string indexing)
print(list[0])

#list slicing
print(list[:3])

#list is immuable

list[3] = "KARAN"
print("After assignment 'k' -> KARAN", list)

#reference copy (Targetting to same memory address)
l = [10,20,30,40,50]
l2 = l
l2[0] = 1000

print(l) # you can see  l is also change but be did changes only in l2
print(l2)

#shallow copy ( Targetting to different memory address)

l = [10,20,30,40,50]
l2 = l.copy()
l2[0] = 1000

print(l) # you can see  l is not changes 
print(l2)

#List traversing

list = [10,30,50,70,90,110, 130, 150, 170, 190, 200]

#method 1
print("Method 1 of list traversal")
for elem in list:
    print(elem)

#method 2
print("Method 2 of list traversal")
for i in range(len(list)):
    print(list[i])

#metho 3
print("Method 3 of list traversal")
for index, value in enumerate(list):
    print(index, " -> ", value)


#string functions

'''
append() - add at last
pop() - remove at last and also from index and get removed value
len() - to get length
lst.insert(1, 50) -   50 in index 1
lst.clear() - remove all 
lst.sort(reverse = true) - asc and desc
lst.reverse() - to reverse
lst.index() - get specific index by value

'''