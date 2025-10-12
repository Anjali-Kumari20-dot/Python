import random

def roll():
    max_value = 6
    min_value = 1

    roll = random.randint(min_value, max_value)

    return roll

generate_roll = roll()
print(generate_roll)

while True:
    players = input("Enter a number between 2 and 4: ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4")
    else:
        print("Invalid, try again") 

max_score = 50 
player_scores = [0 for _ in range(players)]

print(player_scores)
