#guess the number -- Game
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