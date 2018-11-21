number = int(input("Enter the door number, which you will choose:"))
import random
radomString = random.randint(1, 3)
randomString = number
if number == 1:
    print("Now the host will open the third door. Oops, here is a goat))")
    number = int(input("Enter a number again. Will you change your mind? "))
    if number == 2:
        print("Congratulations!!!! You won the car")
    else:
        print("Oops, sorry. You lost your chance:(")
elif number == 2:
    print("Now the host will open the first door. Oops, here is a goat))")
    number = int(input("Enter a number again. Will you change your mind? "))
    if number == 2:
        print("Oops, sorry. You lost your chance:(")