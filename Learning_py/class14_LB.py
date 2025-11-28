# count the frequency of each number given in list

#Solution 1 
list = [1,1,1,2,2,2,2,3,5,5,5,6,6,6,1,1,2,3,5,6,6,7,8,9,1,2,3,4,5]
dic = {}

for item in list:
    if(dic.get(item)):
        dic[item] = dic.get(item)+1
    else:
        dic[item] = 1
        
print("Solution - 1", dic)

#Solution 2
list = [1,1,1,2,2,2,2,3,5,5,5,6,6,6,1,1,2,3,5,6,6,7,8,9,1,2,3,4,5]
dic = {}

for item in list:
    if(item in dic.keys()):
        dic[item] +=1
    else:
        dic[item] = 1
        
print("Solution -2 ", dic)

