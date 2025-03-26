while True:

    want_instructions = input("Do you wan to see the instructions? ").lower()

     # check the user says yes / no
    if want_instructions == "yes" or want_instructions == "y":
        print("you said yes")
        break
    elif want_instructions == "no":
        print ("you said no")
        break
    else:
        print("please enter yes / no")
        continue

print("we done")
