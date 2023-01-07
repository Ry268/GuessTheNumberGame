import random

while True:
    try:
        n = int(input("Please enter the minimum value:- "))
        m = int(input("Please enter the maximum value:- "))
        break
    except:
        print("Please enther the number")

while m < n:
    m = int(input("Please enter a value greater than or equal to the minimum value:- "))

x = random.randint(n, m)

chance = 5

count = 0

print(f"You have {chance} challenges.")

while count < chance:
    count += 1
    print(f"{count} attempt")
    while True:
        try:
            answer = int(input("Guess a number:- "))
            break
        except:
            print("Please enther the number")
            continue

    if answer == x:
        print(f"Congratulations number is {x}")
        break
    elif answer < x:
        print("You guessed too small!")
    else:
        print("You Guessed too high!")

if count == chance:
    print("You Lose")