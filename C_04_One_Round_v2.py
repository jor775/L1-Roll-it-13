import random


def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    #Roll the dice for the user and note if they got a double
    roll_one = random.randint(1,6)
    roll_two = random.randint(1,6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total} ")

    return total, double


#main routine starts here...


#Roll the dice for the user and note if they got a double
initial_user = initial_points("user")
initial_comp = initial_points("comp")

#retrive user points (first item returned from function)
user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user[1]

# let the user know if they qualify for double points
if double_user == "yes":
    print("Great news - if you win, you will earn double points! ")

#assume user goes first...
first = "User"
second = "Computer"
player_1_points = user_points
player_2_points = comp_points

#if the user has fewer points, they start the game
if user_points < comp_points:
    print("You start because your initial roll was less than the computer\n")

#if the user and computer roll equal points, the user is player 1...
elif user_points == comp_points:
    print("the initial rolls were the same, the user starts!")

#if the computer has fewer points, switch the computer to 'player 1'
else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first,second = second, first

#Loop until we have a winner...
while player_1_points < 13 and player_2_points < 13:
    print()
    input("Print <enter> to continue this round\n")

    # first player rolls the die and score is updated
    player_1_roll = random.randint(1,6)
    player_1_points += player_1_roll


    print(f"{first}: rolled a {player_1_roll} - f has {player_1_points} points")

    # if the first person's score is over 13, end the round
    if player_1_points >= 13:
        break

    # second person rolls rhe die (and score is updated)
    player_2_roll = random.randint(1,6)
    player_2_points += player_2_roll

    print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

    print(f"{first}: {player_1_points} | {second} {player_2_points}")
#End of round

#associate player points with either the user or the computer
user_points = player_1_points
comp_points = player_2_points

#switch the user and computer points if the user went fist
if first == "Computer":
    user_points, comp_points = comp_points, user_points

#work out who won...
if user_points > comp_points:
    winner = "user"
else:
    winner = "computer"

round_feedback = f"The user {winner} won. "

# double user points if eligible
if winner == "user" and double_user == "yes":
    user_points = user_points * 2

# Output round results
print("\nRound Results")
print(f"User points: {user_points} | computer Points: {comp_points}")
print(round_feedback)
print()

