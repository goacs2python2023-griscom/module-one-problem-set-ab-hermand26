import random

def sumDice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    sum = int(roll1) + int(roll2)
    if sum >= 6 and sum <= 8:
        return 'Win'
    else:
        return 'Lose'

print(sumDice())