from Game import Game
from Player import Player

while True:
    p1 = Player()
    p2 = Player()
    if p1 != p2:
        break

game = Game(p1, p2)
game.start()