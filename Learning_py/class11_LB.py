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
