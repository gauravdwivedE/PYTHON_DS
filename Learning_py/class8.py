'''
while loop 
break
continue
for....else
'''

#while loop
i = 30
while (i>20):
    print(i)
    i-=1

#Break and continue
for i in range(40):
    if i == 5:
     break
    if i == 10:
       continue
    print("Hula")

#for... else
#if break does not exucute then else executes
for i in range(10):
    if i == 11:
     break
else:
   print("Break executed")


#Problem print first digit of aa number = 145 => 1, 321 => 3
n = int(input("Enter number "))
temp = n
ans = 0
while(n > 0):

   ans = n % 10
   n = n // 10

print(f"First digit of {temp} is {ans}")

#Reverse a number
n = int(input("Enter number to reverse "))
rev = 0

while(n > 0):
    rev = rev * 10 + n % 10
    n = n // 10

print(f"Rev of your digit is {rev}")