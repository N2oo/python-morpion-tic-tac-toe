class Playfield:
    def __init__(self):
        self.playfield = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    def __str__(self):
        result = ""
        result = result[:-1] + "\n"
        for row in self.playfield:
            for square in row:
                result += str(square) + "|"
            result = result[:-1] + "\n"
        return result

    def isCaseAvailable(self, number: int) -> bool:
        for line in self.playfield:
            for element in line:
                if str(element) == str(number):
                    return True
        return False

    def isLineWinner(self) -> str or bool:
        for line in self.playfield:
            if line[0] == line[1] == line[2]:
                return line[0]
        return False

    def isColumnWinner(self) -> str or bool:
        for i in range(3):
            if self.playfield[0][i] == self.playfield[1][i] == self.playfield[2][i]:
                return self.playfield[0][i]
        return False

    def isDiagonalWinner(self):
        if self.playfield[0][0] == self.playfield[1][1] == self.playfield[2][2]:
            return self.playfield[1][1]
        if self.playfield[0][2] == self.playfield[1][1] == self.playfield[2][0]:
            return self.playfield[1][1]
        return False

    def gameIsWinned(self):
        gameIsWinned = self.isLineWinner() or self.isColumnWinner() or self.isDiagonalWinner()
        if gameIsWinned:
            return self.getWinner()
        return False

    def getWinner(self):
        if self.isLineWinner():
            return self.isLineWinner()
        if self.isColumnWinner():
            return self.isColumnWinner()
        if self.isDiagonalWinner():
            return self.isDiagonalWinner()

    def place(self, symbol: str, position: int):
        for i in range(3):
            for j in range(3):
                if str(self.playfield[i][j]) == str(position):
                    self.playfield[i][j] = symbol
                    return True
        return False
