import random

class Game:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def show_board(self):
        print(self.board[0], "|", self.board[1], "|", self.board[2])
        print("--+---+--")
        print(self.board[3], "|", self.board[4], "|", self.board[5])
        print("--+---+--")
        print(self.board[6], "|", self.board[7], "|", self.board[8])

    def make_move(self, pos):
        if self.board[pos] == " ":
            self.board[pos] = self.current_player
            return True
        return False

    def check_win(self):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return True
        return False

    def is_draw(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def move(self, board):
        pos = int(input("Введите номер клетки (0-8): "))
        return pos



class EasyBot(Player):
    def move(self, board):
        free_cells = []
        for i in range(9):
            if board[i] == " ":
                free_cells.append(i)
        return random.choice(free_cells)

game = Game()
player1 = Player("X")
bot = EasyBot("O")


class MediumBot(Player):
    def move(self, board):
        for i in range(9):
            if board[i] == " ":
                board[i] = self.symbol
                if self.check_winner(board, self.symbol):
                    board[i] = " "
                    return i
                board[i] = " "

        enemy  = "X" if self.symbol == "O" else "O"
        for i in range(9):
            if board[i] == " ":
                board[i] = enemy
                if self.check_winner(board, enemy):
                    board[i] = " "
                    return i
                board[i] = " "

        free_cells = []
        for i in range(9):
            if board[i] == " ":
                free_cells.append(i)

        return random.choice(free_cells)
    def check_winner(self, board, symbol):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a, b, c in wins:
            if board[a] == board[b] == board[c] == symbol:
                return True
        return False

class HardBot(Player):
    def move(self, board):
        best_score = -100
        best_move = None

        for i in range(9):
            if board[i] == " ":
                board[i] = self.symbol
                score = self.minimax(board, False)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move

    def minimax(self, board, is_max):
        if self.check_winner(board, self.symbol):
            return 1
        if self.check_winner(board, "X"):
            return -1
        if " " not in board:
            return 0
        if is_max:
            best = -100
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.symbol
                    score = self.minimax(board, False)
                    board[i] = " "
                    best = max(best, score)
            return best
        else:
            best = 100
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = self.minimax(board, True)
                    board[i] = " "
                    best = min(best, score)
            return best
    def check_winner(self, board, symbol):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a, b, c in wins:
            if board[a] == board[b] == board[c] == symbol:
                return True
        return False



def choose_bot_difficulty(bot_number):
    print(f"Виберите сложность бота {bot_number}:")
    print("1 - Легкий")
    print("2 - Средний")
    print("3 - Сложний")

    choice = input("Введите номер (1-3): ")
    while choice not in ("1", "2", "3"):
        choice = input("Неверний ввод. Введите номер (1-3): ")
    return int(choice)

def create_bot(difficulty, symbol):
    if difficulty == 1:
        return EasyBot(symbol)
    elif difficulty == 2:
        return MediumBot(symbol)
    elif difficulty == 3:
        return HardBot(symbol)

player = Player("X")
bot_difficulty = choose_bot_difficulty(1)
bot = create_bot(bot_difficulty, "O")

game = Game()

while True:
    game.show_board()

    if game.current_player == "X":
        pos = player.move(game.board)
    else:
        pos = bot.move(game.board)

    if not game.make_move(pos):
        print("Клетка занята!")
        continue

    print(f"Ход сделал: {game.current_player}\n")

    if game.check_win():
        game.show_board()
        print("Победил игрок!", game.current_player)
        break

    if game.is_draw():
        game.show_board()
        print("Ничья!")
        break

    game.switch_player()

