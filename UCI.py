import chess
import engine

ENGINENAME = "BetaZero"
AUTHOR = "ADAM DERYLO"


class UCI:

    @staticmethod
    def uciCommunication():
        board = chess.Board()
        while True:
            inputString = input()

            if inputString == "uci":
                inputUCI()

            elif inputString.split()[0] == "setoption":
                inputSetOption(inputString)

            elif inputString == "isready":
                inputIsReady()

            elif inputString == "ucinewgame":
                inputUCINewGame(board)

            elif inputString.split()[0] == "position":
                board = inputPosition(inputString)

            elif inputString.split()[0] == "go":
                inputGo(board)

            elif inputString == "print":
                inputPrint(board)

            elif inputString == "quit":
                print("yooyoyo")
                break


def inputUCI():
    print("id name " + ENGINENAME)
    print("id author " + AUTHOR)
    # options go here
    print("uicok\n")


def inputSetOption(input):
    # here should be possible changes in options
    print("none yet")


def inputIsReady():
    print("readyok")


def inputUCINewGame(board):
    board = chess.Board()


def inputPosition(string):
    board = chess.Board()
    string = str(string)
    string = string.strip()
    string = string[8:].strip()

    if string.startswith("startpos"):
        string = string[8:].strip()

    elif string.startswith("fen"):
        string = string[3:].strip()
        board = chess.Board(string)

    if string.startswith("moves"):
        string = string[5:].strip()

        while string:
            x = string.find(" ")
            if x == -1:
                move = chess.Move.from_uci(string.strip())
                board.push(move)
                break

            else:
                move = chess.Move.from_uci(string[:x].strip())
                board.push(move)
                string = string[x:].strip()

    return board


def inputGo(board):
    print("bestmove " + engine.enigne.random_move(board))


def inputPrint(board):
    print(board)
