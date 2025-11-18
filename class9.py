#guess the number -- Game
'''
import random as r

randome = r.randint(1, 100)
print("System has generated a randome number")
tries = 0
while True:
    n = int(input("Enter your guess"))
    tries += 1
    if n == randome:
        print(f"Congrats you guess it in {tries} tries")
        break
    elif n > randome:
        print("Go little lower")
    else:
        print("Go little upper")

'''

# stone paper scissors game
import random

u_point = 0
s_point = 0



while True:
    if s_point == 5 or u_point == 5:
        break
     
    user = int(input("Enter 1 for stone, 2 for paper, 3 for scissors "))
    system = random.randint(1,3)

    if (not user >=1 or not user <=3):
        continue
    
    print("You ", user)
    print("System", system)


    if user == system:
        print("Both are equal")
    elif system == 1 and user == 3:
        print("system win")
        s_point += 1

    elif system == 2 and user == 1:
        print("system win")
        s_point += 1

    elif system == 3 and user == 2:
        print("system win")
        s_point += 1

    else:
        print("You win ")
        u_point += 1

print("Your's point = ", u_point)
print("System's point = ", s_point)