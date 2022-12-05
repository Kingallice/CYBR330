import copy

class TicTacToe:

    def __init__(self, board = None):
        if not board:
            self._board = [[None, None, None],[None, None, None], [None, None, None]]
        else:
            self._board = board

    def runGame(self):
        try:
            player = 'NULL'
            bot = 'x'
            while player not in 'xo':
                player = input("Welcome to Tic Tac Toe!\nWould you like to be x's or o's? ").lower()
                if player == 'x':
                    bot = 'o'
                elif player == 'o':
                    bot = 'x'
            winner = None
            while not winner:
                if self.getTurn() == player:
                    print(self)
                    self.playerInput()#self.playerInput()
                elif self.getTurn() == bot:
                    self.minimax(bot)
                winner = self.checkWin()
            print(self, "\nWinner:", winner)
        except:
            pass                

    def playerInput(self):
        place = None
        while not type(place) == type(list):
            place = input("Where would you like to play row[0-2] column[0-2] - (x,y)? ")
            place = place.replace('(', '')
            place = place.replace(')', '')
            place = place.split(',')
            if len(place) == 2:
                try:
                    self.setPosistion(int(place[0]), int(place[1]))
                    break
                except:
                    print(Exception)

    def minimax(self, bot):
        if self.checkWin():
            return self.rankState(bot)
        moves, scores = [], []

        for move in self.possibleMoves():
            temp = self.copy()
            temp.setPosistion(move[0], move[1])
            scores.append(temp.minimax(bot))
            moves.append(move)

        if self.getTurn() == bot:
            max_idx = scores.index(max(scores))
            move = moves[max_idx]
            self.setPosistion(move[0],move[1])
            return scores[max_idx]
        else:
            min_idx = scores.index(min(scores))
            move = moves[min_idx]
            self.setPosistion(move[0],move[1])
            return scores[min_idx]

    def rankState(self, bot):
        winner = self.checkWin()
        if not winner:
            return 0
        if winner == bot:
            return 1
        elif winner != "No one" and winner != bot:
            return -1
        return 0

    def possibleMoves(self):
        state = self.getBoard()
        for i in range(len(state)):
            for j in range(len(state[i])):
                if not state[i][j]:
                    yield (i, j)

    def setPosistion(self, x, y):
        numX, numO = 0, 0
        for row in self._board:
            for item in row:
                if item == "x":
                    numX += 1
                elif item == "o" :
                    numO += 1
        move = "x"
        if numX > numO:
            move = "o"
        if self._board[x][y] == None:
            self._board[x][y] = move
        else:
            raise Exception("Location already populated!")

    def checkWin(self):
        state = self.getBoard()
        players = 'xo'
        for i in range(len(state)):
            line = []
            for j in range(len(state[i])):
                line.append(state[i][j])
                for p in players:
                    if line.count(p) == 3:
                        return p
        for i in range(len(state[0])):
            line = []
            for j in range(len(state)):
                line.append(state[j][i])
                for p in players:
                    if line.count(p) == 3:
                        return p
        line = []
        for i in range(len(state)):
            line.append(state[i][i])
            for p in players:
                if line.count(p) == 3:
                    return p
        line = []
        for i in range(len(state)):
            line.append(state[2+(i*-1)][i])
            for p in players:
                if line.count(p) == 3:
                    return p
        if len([x for x in self.possibleMoves()]) == 0:
            return "No one"
        return None

    def getTurn(self):
        numX, numO = 0, 0
        if len([move for move in self.possibleMoves()]) == 0:
            return
        for row in self._board:
            for item in row:
                if item == "x":
                    numX += 1
                elif item == "o" :
                    numO += 1
        if numX > numO:
            return "o"
        return "x"

    def getBoard(self):
        return copy.deepcopy(self._board)

    def copy(self):
        return TicTacToe(self.getBoard())

    def __str__(self):
        out = ""
        for x in self._board:
            out += "["
            for y in x:
                out += " "
                if y == None:
                    out += "-"
                else: 
                    out += str(y)
                out += " "
            out += "]\n"
        return out

while True:
    TicTacToe().runGame()
    if input("\nWould you like to play again? (y/n) ").lower() == 'n':
        break