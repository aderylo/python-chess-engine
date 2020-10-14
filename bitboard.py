import chess


# following function transforms FEN notation into bitboard one;
# biboard depicts chess posisition by asgining to each squere sequence of 12 bits
'''
 1 followed by 11 zeros == white pawn 
 01 followed by 10 zeros == white knight 
 by the same rule bishop, rock, queen and king are depicted later 6 zeros are rezerved for black peaces 

if squere is depicted by 12 zeros then it is empty 

we start depiciting board from squere A1 and then from left to right row by row; 
after this 5 additional bits tell us whoes move ("1" white, "0" black)
and castling rights KQkq(look up FEN notation)

'''


def fentobit(fen):
    end = str.find(fen, " ")
    bit = ""
    for x in range(0, end):
        a = fen[x]

        if a == "P":
            b = "100000000000"
        elif a == "N":
            b = "010000000000"
        elif a == "B":
            b = "001000000000"
        elif a == "R":
            b = "000100000000"
        elif a == "Q":
            b = "000010000000"
        elif a == "K":
            b = "000001000000"
        elif a == "p":
            b = "000000100000"
        elif a == "n":
            b = "000000010000"
        elif a == "b":
            b = "000000001000"
        elif a == "r":
            b = "000000000100"
        elif a == "q":
            b = "000000000010"
        elif a == "k":
            b = "000000000001"
        elif a != "/":
            b = ""
            for i in range(0, int(a)):
                b = b + "000000000000"
        elif a == "/":
            b = ""

        bit = bit + b

    # reversing as we want bitboard that starts from A1 square not A8
    pos = ""
    for x in range(8, 0, -1):
        pos = pos + bit[(x-1)*96:x*96]

    # whose move?
    if str.find(fen, "w") == -1:
        pos = pos + "0"
    else:
        pos = pos + "1"

    # castling rights:
    rest = fen[end:]
    if str.find(rest, "K") == -1:
        pos = pos + "0"
    else:
        pos = pos + "1"

    if str.find(rest, "Q") == -1:
        pos = pos + "0"
    else:
        pos = pos + "1"

    if str.find(rest, "k") == -1:
        pos = pos + "0"
    else:
        pos = pos + "1"

    if str.find(rest, "q") == -1:
        pos = pos + "0"
    else:
        pos = pos + "1"

    return pos
