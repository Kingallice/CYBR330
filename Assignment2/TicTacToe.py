class TicTacToe:

    def __init__(self):
        self._board = [[None, None, None],[None, None, None], [None, None, None]]
        self.runGame()

    def runGame(self):
        try:
            player = 'NULL'
            while player not in 'xo':
                player = input("Welcome to Tic Tac Toe!\nWould you like to be x's or o's? ").lower()
            while not self.checkWin():
                if player == 'x':
                    self.playerInput()
        except:
            pass                

    def playerInput(self):
        place = None
        while not type(place) == type(list):
            print(self)
            place = input("Where would you like to play row[0-2] column[0-2] - (x,y)? ")
            place = place.replace('(', '')
            place = place.replace(')', '')
            place = place.split(',')
            if len(place) == 2:
                try:
                    self.setPosistion(int(place[0]), int(place[1]))
                    break
                except:
                    pass

    def botInput(self, bot):
        pass

    def findBestMove():
        pass

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
        players = 'xo'
        for i in range(len(self._board)):
            line = []
            for j in range(len(self._board[i])):
                line.append(self._board[i][j])
                for p in players:
                    if line.count(p) == 3:
                        return p
        for i in range(len(self._board[0])):
            line = []
            for j in range(len(self._board)):
                line.append(self._board[i][j])
                for p in players:
                    if line.count(p) == 3:
                        return p
        line = []
        for i in range(len(self._board)):
            line.append(self._board[i][i])
            for p in players:
                if line.count(p) == 3:
                    return p
        line = []
        for i in range(len(self._board)):
            line.append(self._board[2+(i*-1)][i])
            for p in players:
                if line.count(p) == 3:
                    return p
        return None

    def __copy__(self):
        return self.copy()

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

x = TicTacToe()