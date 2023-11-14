from Player import Player
from Playfield import Playfield


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.playfield = Playfield()
        self.player1 = player1
        self.player2 = player2

    def translatePlayer(self,symbol:str)->Player:
        if symbol == self.player1:
            return self.player1
        return self.player2

    def makePlayerPlay(self,player:Player)->Player or False:
        while True:
            case = player.play()
            if self.playfield.isCaseAvailable(case):
                self.playfield.place(player.symbole,case)
                break
            else:
                print("La case n'est pas disponible, veuillez resaisir une case !")

    def start(self):
        winner = None
        cnt = 1
        while True:
            print(self.playfield)
            if cnt %2 == 0:
                self.makePlayerPlay(self.player1)
            else:
                self.makePlayerPlay(self.player2)
            gameWinned = self.playfield.gameIsWinned()
            if gameWinned:
                winner = self.translatePlayer(gameWinned)
                break
            cnt+= 1
        print("Félicitations le jeu a été remporté par {}".format(winner))
        print(self.playfield)