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
            return (GamePoints.LOSS.value, 'Z')
        if me == 'Y':
            return (GamePoints.DRAW.value, 'X')
        if me == 'Z':
            return (GamePoints.WIN.value, 'Y')
    if opponent == 'B':
        if me == 'X':
            return (GamePoints.LOSS.value, 'X')
        if me == 'Y':
            return (GamePoints.DRAW.value, 'Y')
        if me == 'Z':
            return (GamePoints.WIN.value, 'Z')
    if opponent == 'C':
        if me == 'X':
            return (GamePoints.LOSS.value, 'Y')
        if me == 'Y':
            return (GamePoints.DRAW.value, 'Z')
        if me == 'Z':
            return (GamePoints.WIN.value, 'X')

def gameOutCome(opponent, me):
    pts = 0
    (_pts, _me) = win_loss(opponent, me)
    if _me == str(GamePoints.X.name):
        pts+=GamePoints.X.value
    if _me == str(GamePoints.Y.name):
        pts+=GamePoints.Y.value
    if _me == str(GamePoints.Z.name):
        pts+=GamePoints.Z.value
    pts+= _pts
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