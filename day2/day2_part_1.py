from enum import Enum
import math

""" 
OPPONENT
A = ROCK
B = PAPER
C = SCISSORS

MINE
X = ROCK
Y = PAPER
Z = SCISSORS

"""
class GamePoints(Enum):
    X = 1
    Y = 2
    Z = 3
    LOSS = 0
    DRAW = 3
    WIN = 6

def win_loss(opponent, me):
    if opponent == 'A':
        if me == 'X':
            return GamePoints.DRAW.value
        if me == 'Y':
            return GamePoints.WIN.value
        if me == 'Z':
            return GamePoints.LOSS.value
    if opponent == 'B':
        if me == 'X':
            return GamePoints.LOSS.value
        if me == 'Y':
            return GamePoints.DRAW.value
        if me == 'Z':
            return GamePoints.WIN.value
    if opponent == 'C':
        if me == 'X':
            return GamePoints.WIN.value
        if me == 'Y':
            return GamePoints.LOSS.value
        if me == 'Z':
            return GamePoints.DRAW.value

def gameOutCome(opponent, me):
    pts = 0
    if me == str(GamePoints.X.name):
        pts+=GamePoints.X.value
    if me == str(GamePoints.Y.name):
        pts+=GamePoints.Y.value
    if me == str(GamePoints.Z.name):
        pts+=GamePoints.Z.value
    pts+= win_loss(opponent, me)
    return pts

allGames = []
with open("input_1.txt", 'r') as file:
    for game in file.read().splitlines():
        oneGame = game.split(' ')
        allGames.append(oneGame)

totalScore = []
for game in allGames:
    opponent = game[0]
    me = game[1]
    gamePts = gameOutCome(opponent, me)
    totalScore.append(int(gamePts))
print(f'Total game score: {math.fsum(totalScore)}')