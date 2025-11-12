''' 
Strings
Strings sclicing
Formatted strings
space sequences
Raw strings
truthy and falsy values
type conerstion
input from user
'''

#String and String Slicing
a = "Hello i am data scientist"

print(a[0:5])
print(a[11:15])
print(a[16: ])

print(r"this is raw string \n \b \t");

# falsy values = 0, 0.0, false, [], (), {}
# truty values = everything excluding from falsy values

#input 
city = input("Enter your city")
print(city)

#type conersion 
# int(), float(), bool(), str()

car_rent = float(input("Enter your car rent/month"))
month = float(input("Enter your months you drove"))

print(f"Your final bill is  {car_rent * month}")