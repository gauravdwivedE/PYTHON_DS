#Find largest elem in list
list = [10,20,40,50,30,20,66, 66.0,10,60,65,45,40,12,56,23,56]
max = 0
for index,value in enumerate(list):
    if(value > max):
        max = value

print("largest = ", max)

#Second largest
list = [10,20,40,50,30,20,66,10,60,65,45,40,12,56,23,56]
max = 0
second_max = 0

for i in range(len(list)):
    if list[i] > max:
        second_max = max
        max = list[i]

    elif (list[i] > second_max and list[i] < max):
        second_max = list[i]

print("Second largest = ", second_max)

#check list is shorted or not (increasing order)
list = [1,2,13,4,5]
verify = True

for i in range(len(list) -1 ):
    if(list[i] > list[i+1]):
        verify = False
        break

print(verify)

#array left rotation by 1
list = [1,2,13,4,5,55,11,22]
print("Before = ", list)

for i in range(len(list) -1):
    list[i+1], list[i] = list[i], list[i+1]

print("After = ", list)

#reverse list without using extra space
list = [1,2,3,4,5,6,7,8,9,10]
str = 0
end = len(list) - 1

while(str < end):
    list[str], list[end] = list[end], list[str]
    str += 1
    end -= 1 

print("Reversed list = " ,list)


#linear search
# list = [1,2,3,4,5,6,7,8,9,10]
# elem = int(input("Enter elem that you want to search "))

# for item in list:
#     if(elem == item):
#         print("--- Found ---")
#         break;

#binary search
list = [10,20,30,40,50,60,70,80,90,100]

index = -1
elem = 0

str = 0
end = len(list) - 1

while(str <= end):
    mid = str+end // 2
    if(list[mid] == elem):
        index = mid
        break
    elif(elem > list[mid]):
       str = mid +1
    else: 
        end = mid - 1 
       
if(index >=0 ):
    print("Found at ", index)
else:
    print("Not found")