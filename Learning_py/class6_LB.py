'''
check leap year
check char is vowel or not
'''

#check leap year
year = int(input("Enter year "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
    print("Leap year")
else:
    print("Normal year")


#check char is vowel or not
char = input("Enter single char")

if(char in "aeiouAeiou"):
    print("vowel")
else:
    print("consonent")

