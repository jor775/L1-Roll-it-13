from C_03_integer_checker_v1 import game_goal


def int_check():
    """Checks users enter an integer more than / equal to 13"""

    error = "please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("What is the game goal? "))

            if response < 13:
                print(error)
            else:
                print(f"game goal: {response} ")
            return

        except ValueError:
            print(error)


# main routine starts here
game_goal = int_check()
print(game_goal)
