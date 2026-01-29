'''
Lambda function 
map, filter, zip
'''

#creating a lamda function

sum = lambda a,b,c : a+b+c
print(sum(10,20,30))


#using map 

marks = [10, 20, 40,10,50,10,80,10,40]

newMarks = list(map(lambda item : item*2, marks))
print(newMarks)

#using filter want to remove marks greater 100

newMarks = list(filter(lambda item : 100 >= item, newMarks))
print(newMarks)

# using zip combining 3 lists

names = ["guarav", "shivam", "manoj", "ishita", "adhya"]
marks = [10, 20, 40,10,50,10,80,10,40]
ages = [20, 34, 12, 23, 9]

comb = list(zip(names, marks, ages))

print(comb)
