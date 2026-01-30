'''
Lambda function 
map, filter, zip
list/set/dic comprehension in python
generator comprehension
Decorator
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

#list comprehension. -> want to store count greater than 10 (even we can do this tast using filter
#but still for some cases we should know about it)

chairsCount = [1,2,3,4,5,6,3,4,56,54,5,4,34,64]

newChairsCount = [i for i in chairsCount if i > 10]
print(newChairsCount)

#stack comprehension. -> want to store count greater than 10 (even we can do this tast using filter
#but still for some cases we should know about it)

chairsCount = {1,2,3,4,5,6,3,4,56,56,5,4,34,64}

newChairsCount = {i for i in chairsCount if i > 10}
print(newChairsCount)



#dic comprehension.
chairsCount = {1,2,3,4,5,6,3,4,56,56,5,4,34,64}

newChairsCount = {i:i*10 for i in chairsCount}
print(newChairsCount)


#generator


#Decorator

def test_decorator(func):
    def wrapper(a,b): # getting args from decorator
        print("I will run defore sum()");
        func(a,b) #running sum which is stored in func
        print("I will run after sum()");
    return wrapper # calling wrapper
        
    




@test_decorator
def sum(a,b):
    print(a+b);

sum(10,30)
