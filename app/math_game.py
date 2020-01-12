# (c) 2020 Simon Averbach and Zev Averbach
from time import sleep

from config import MAX_NUM, DEFAULT_COUNTING_SPEED


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

    print(f"How many counts do you want to do per second? [{DEFAULT_COUNTING_SPEED:,}]")
    num_counts_per_second_string = input("> ")
    if num_counts_per_second_string == '':
        num_counts_per_second = DEFAULT_COUNTING_SPEED
    else:
        num_counts_per_second = int(num_counts_per_second_string)

    print(f"Okay, here we go! We're going to count from zero to {number}, "
          f"adding {each} {num_counts_per_second} times per second.")
    sleep(3)
    sleep_for_seconds_between_counts = 1 / num_counts_per_second
    for i in range(1, number + 1, each):
        print(f"{i:,}")
        sleep(sleep_for_seconds_between_counts)


if __name__ == "__main__":
    math_game()
