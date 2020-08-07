def jumpingOnClouds(c):
    clouds = len(c)
    jumps = 0
    counter = 0
    while counter < clouds:
        # if counter + 2 < clouds:
        try:
            if c[counter + 2] != 1:
                counter += 2
            else:
                counter += 1

            jumps += 1
        except:
            if counter + 1 < clouds and c[counter + 1] != 1:
                counter += 1
                jumps += 1
            else:
                return jumps

    return jumps


if __name__ == "__main__":
    # print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
    print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
