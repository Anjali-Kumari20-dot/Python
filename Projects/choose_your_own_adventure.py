name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

first_choice = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if first_choice == "left" :
    river_choice = input("You come to a river, you can walk around or swim accross.").lower()

    if river_choice == "swim":
        print("You swam accross and were eaten by an alligator.")
    elif river_choice == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif first_choice == "right":
    bridge_choice = input("You come to a bridge, it looks wobbly, do you wamt to cross it or head back (cross/back)?")

    if bridge_choice == "back":
        print("You go back and lose.")
    elif bridge_choice == "cross":
        stranger_choice = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()

        if stranger_choice == "yes":
            print("You talk to the stranger and they give the gold. You WIN!")
        elif stranger_choice == "no":
            print("You ignored the stranger and they got offended. You LOSE!")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid path. You lose.")
else :
    print("Not a valid option. You lose.")

print("Thank You for trying ", name, " :)")