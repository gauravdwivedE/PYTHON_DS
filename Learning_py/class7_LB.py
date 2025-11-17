
#count number of lower and uppercase values

str = "GauRAV"

count_upper = 0
count_lower = 0


for char in str:
     if char.isupper():
          count_upper += 1
     if char.islower():      # not writing else because we only want to check string chars not like 1,4,4,#%^&*? etc.
        count_lower += 1

print(count_lower, count_upper)