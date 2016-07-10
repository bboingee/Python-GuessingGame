import random

num = random.randint(1, 10)
print(num)
tries = 0
while True:
    try:
        guess = int(input("Guess number from 1 to 10, You get 3 tries : "))
        if guess in range(1, 11):
            if guess == num:
                exit("You have guessed the number right")
            elif tries < 2:
                print("You have guessed the wrong number")
                tries += 1
                if guess - 1 <= num <= guess + 1:
                    print("Hot")
                elif guess - 2 <= num <= guess + 2:
                    print("Warm")
                else:
                    print("Cold")
            else:
                exit("You have failed to guess the number")
        else:
            raise IOError

    except ValueError:
        print("You did not enter an numerical number")
    except IOError:
        print("You did not enter within range")
