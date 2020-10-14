# this script cuts pgn from computerengines website into smaller peaces as it is to big to be handeled


with open("gig", 'r') as file:
    i = 0
    T = []
    k = 0
    x = 1
    for row in file:

        i += 1
        T.append(row)

        if len(row) == 1:
            k += 1

        if k == 2:
            k = 0
            if i > 1000000:
                print(x)
                f1 = open("unzipped/file" + str(x), 'w')
                for line in T:
                    f1.write(line)
                f1.close()
                x += 1
                i = 0
                T = []
