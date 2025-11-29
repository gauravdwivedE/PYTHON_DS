# 1.count the frequency of each number given in list
#leet code 771 (did in leetoce)
#leetcode 1832 (did in leetcode)
#leetcode 2351 (did in leetcode)

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

#leetcode 1832

'''class Solution(object):
    def checkIfPangram(self, sentence):
        dec = {}
        for item in sentence:
            if(item in dec.keys()):
                dec[item] +=1
            else:
                dec[item] = 1
        if(len(dec) == 26):
            return True
        else:
            return False'''

#leetcode 2351
'''
class Solution(object):
    def repeatedCharacter(self, s):
        dic = {}
        for i in s:
            if(dic.get(i)):
                return i
            else:
                dic[i] = 1
'''