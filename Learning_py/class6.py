'''
if..else statements
pass (if we don't want to write anything in if block)
Turnary operator
'''


#if..else
car_driven = float(input("Enter the KM that car has driven"))

if car_driven > 40000:
    print("Sorry not suitable for us")
else:
    print("Suitable for us")


#pass
shoes_no = 10

if shoes_no >= 9:
    pass
else:
    print("Available")

#Turnany operator
age = 19
print("vote") if age > 20 else print("Can't vote")