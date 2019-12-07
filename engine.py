import chess
import random


class enigne:

    @staticmethod
    def random_move(board):
        M = MoveList(board)
        x = random.randint(0, board.legal_moves.count()-1)

        return str(M[x])


def MoveList(board):
    string = str(board.legal_moves)
    s = string.find('(')
    k = len(string)-2
    string = string[s+1:k]
    string = string + ','
    M = []
    for moves in board.legal_moves:
        cut = string.find(',')
        M.append(board.parse_san(string[0:cut]))
        string = string[cut+2:]
    return M
