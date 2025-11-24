'''
Dictionary  key-values pairs, mutable, can store duplicates
Dictionary constructor
'''
#creating a dictionary
dic = {
    "name": "gaurav",
    "age": 25,
    400: 10000
}

print(dic[400])
dic['age'] = 20
print(dic)

#dict constructor
dic1 = dict(name = "gaurav", age = 100)
print(dic1)

#traversing
dic = {10:1000, 20:2000, 30:3000, 40:4000}

#1
for items in dic.values():
    print(items)

print("Method 2 ")
#2
for i in dic:
    print(dic[i])