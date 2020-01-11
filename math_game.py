# copyright 2020 Simon Averbach and Zev Averbach

def math_game():
    # TODO: make this into a web game, so we can make the numbers bigger
    # TODO: make a warning, or maybe prevent the user from making a count that's 
    # going to take longer than five minutes
    print("Hi, welcome to math game!")
    print("How high do you want to count?")
    number = int(input("> "))
    print("How much do you want to add each time?")
    each = int(input("> "))
    print(f"Okay, here we go! We're going to count from zero to {number} by {each} at a time.")
    sleep(3)
    for i in range(0, number, each):
        print(f"{i:,}")
