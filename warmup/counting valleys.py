

def countingValleys(n, s):
    sea_level = 0
    valleys = 0
    mountains = 0
    moves = []
    counter = 0
    for i in s:

        if i == "U":
            sea_level += 1
            moves.append(sea_level)
        if i == "D":
            sea_level -= 1
            moves.append(sea_level)

        if sea_level == 0 and moves:
            total = sum(moves)
            if total > 0:
                mountains += 1
                moves.clear()
            else:
                valleys += 1
                moves.clear()

    return valleys


if __name__ == "__main__":
    # countingValleys(2, "DDUUDDUDUUUD")
    print(countingValleys(8, "UDDDUDUU"))
