# copyright 2020 Simon Averbach and Zev Averbach
from config import MAX_NUM


def math_game():
    for i in range(100):
        print()
    print("Hi, welcome to math game!")
    print("How high do you want to count?")
    number = int(input("> "))
    while number > MAX_NUM:
        print(f"Sorry, there's a limit of {MAX_NUM:,}")
        print("How high do you want to count?")
        number = int(input("> "))
    print("How much do you want to add each time?")
    each = int(input("> "))
    print(f"Okay, here we go! We're going to count from zero to {number} by {each} at a time.")
    sleep(3)
    for i in range(0, number, each):
        print(f"{i:,}")


if __name__ == "__main__":
    math_game()
