#At the start of the game, the computer / user score are both zero

comp_score = 0
user_score = 0

game_goal= int(input("Game Goal"))
#Play multiple rounds until a winner has been found
while comp_score <  game_goal and user_score < game_goal:

    #start of round loop
    #for testing purposes,ask the user what the points for the user / computer were
    comp_points = int(input("Enter the computer points at the end of the round: "))
    user_points = int(input("Enter the user points at the end of the round: "))

    #outline rounds loop - Update score with round point,only add points to the score of the
    #show overall scores(add this to round loop)
    print("*** Game update ***")   # replace with call to statement generator
    print(f"User score: {user_score} | Computer score {comp_score}")


#end of entire game, output final results
print()
if user_score > comp_score:
    print("the user won")
else:
    print("The computer won")