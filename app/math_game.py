# (c) 2020 Simon Averbach and Zev Averbach
import math
from time import sleep

from config import MAX_NUM, DEFAULT_COUNTING_SPEED, MAX_RUNNING_TIME_SECONDS


def clear_screen():
    for i in range(100):
        print()


def print_greeting():
    print("Hi, welcome to math game!")


def get_last_number():
    last_number = int(input("How high do you want to count?\n> "))
    while last_number > MAX_NUM:
        print(f"Sorry, there's a limit of {MAX_NUM:,}")
        print("How high do you want to count?")
        last_number = int(input("> "))
    return last_number


def get_increment():
    return int(input("How much do you want to add each time?\n> "))


def predict_running_time(last_number, increment, num_counts_per_second):
    return int((last_number / increment) / num_counts_per_second)


def calculate_suggested_num_counts_per_second(last_number, increment):
    return math.ceil((last_number / increment) / MAX_RUNNING_TIME_SECONDS)


def get_input(message, default_val):
    print(message)
    input_string = input("> ")
    if input_string == '':
        value = default_val
    else:
        value = int(input_string)
    return value


def get_num_counts_per_second(last_number, increment):
    num_counts_per_second = get_input(
        f"How many counts do you want to do per second? [{DEFAULT_COUNTING_SPEED:,}]",
        DEFAULT_COUNTING_SPEED)

    predicted_running_time_seconds = predict_running_time(last_number, increment, num_counts_per_second)

    while predicted_running_time_seconds > MAX_RUNNING_TIME_SECONDS:
        print(f"Sorry, that would run for {predicted_running_time_seconds:,} seconds, which is greater than "
              f"the maximum allowed of {MAX_RUNNING_TIME_SECONDS:,} seconds.")

        suggested_num_counts_per_second = calculate_suggested_num_counts_per_second(last_number, increment)
        print(f"I suggest you run a minimum of {suggested_num_counts_per_second:,} counts per second.")

        num_counts_per_second = get_input(
            f"How many counts do you want to do per second? [{suggested_num_counts_per_second:,}]",
            suggested_num_counts_per_second)

        predicted_running_time_seconds = predict_running_time(last_number, increment, num_counts_per_second)

    return num_counts_per_second


def do_the_count(last_number, increment, num_counts_per_second):
    print(f"Okay, here we go! We're going to count from zero to {last_number:,}, "
          f"adding {increment:,} {num_counts_per_second:,} times per second.")
    sleep(3)
    sleep_for_seconds_between_counts = 1 / num_counts_per_second
    for i in range(1, last_number + 1, increment):
        print(f"{i:,}")
        sleep(sleep_for_seconds_between_counts)


def math_game():
    clear_screen()
    print_greeting()
    last_number = get_last_number()
    increment = get_increment()
    num_counts_per_second = get_num_counts_per_second(last_number, increment)
    do_the_count(last_number, increment, num_counts_per_second)


if __name__ == "__main__":
    math_game()
