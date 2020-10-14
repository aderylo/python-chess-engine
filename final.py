import chess
import bitboard
import random

with open("dataset/file", 'r') as file:
    v = 0
    for row in file:

        if v % 10000 == 0:
            print(v)

        v = v + 1
        if row[1] == ".":  # i.e. it is a move list
            board = chess.Board()
            positions = []
            s = str.split(row)
            # we dont want any draws in our dataset
            if s[len(s)-1] == "1/2-1/2":
                continue
            # pushing moves to the stack
            for i in s:
                if str.find(i, "{") != -1:
                    break
                if str.find(i, ".") == -1:
                    board.push_san(i)
                    pos = bitboard.fentobit(board.fen())
                    positions.append(pos)
            # now choose tenpositions from games that have more than 5 moves
            if board.fullmove_number > 10:
                numbers = random.sample(range(10, len(positions)), 10)
                l = str.find(row, "}")
                result = s[len(s)-1]
                if result == "1-0":
                    f1 = open("dataset/W", 'a')
                else:
                    f1 = open("dataset/L", 'a')

                for i in numbers:
                    f1.write(positions[i] + "\n")

                f1.close()
