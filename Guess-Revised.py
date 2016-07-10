import random  # import library called random to generate random numbers.

"""Functions"""


def answer():  # function to give random variable.
    num = random.randint(1, 10)  # num will store the value.
    print("The number to guess is ", num, ".")  # print the value
    return num


def valid():  # function to check input error.
    entry = True
    while entry:
        try:
            guess = int(input("Please guess a number between 1 - 10 : "))
            if guess in range(1, 11):  # The number is index based. Index starts at 0. 1 up to 11 not including 11.
                return guess
            elif guess not in range(1, 11):  # Out of range.
                raise IOError
            else:
                raise ValueError  # Invalid input.
        except IOError:
            print("You have entered a number that is out of range.")
        except ValueError:
            print("You have entered an invalid input.")


def correct(x):  # Function to match user's input with answer.
    i = 0
    for i in range(0, 3):
        tries = 3 - i
        print("You have ", tries, " tries left.")
        guess = valid()
        if guess == x:
            exit("You have guessed the number right!")
        elif i == 2:
            exit("You have failed to guess the right number.")
        else:
            print("Please try again")
            i += 1  # Add 1 to variable 1, to calculate tries, and to satisfy elif statement.


"""Main"""


def main():
    ran = answer()  # ran variable will hold value from answer.
    correct(ran)  # pass the value in ran to correct function.


"""Only main() after this line"""
main()
