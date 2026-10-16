import random

#a)
scores = {} #create a dictionary to record the scores
i=0
for games in range(20):
    alice_score = random.randint(1, 6)
    bob_score = random.randint(1, 6)
    i+=1
    if alice_score>bob_score:
        scores[i] = ["Alice"]
    elif bob_score>alice_score:
        scores[i] = ["Bob"]
    elif alice_score==bob_score:
        scores[i] = ["Draw"]

print(scores)

#b)
#defining the function
def playing_games():
    #asking inputs from user
    player1 = input("Please enter the name of the first player: ")
    player2 = input("Please enter the name of the second player: ")
    n_games = input("Please enter the number of games: ")

    gamescores = {} #create a dictionary to record the scores
    count = 0
    for games in range(int(n_games)):
        p1 = random.randint(1, 6)
        p2 = random.randint(1, 6)
        count+=1
        if p1>p2:
            gamescores[count] = [player1]
        elif p2>p1:
            gamescores[count] = [player2]
        elif alicp1e_score==p2:
            gamescores[count] = ["Draw"]
    return gamescores

#call the function and print the output
print(playing_games())