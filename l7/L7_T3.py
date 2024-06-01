def paths(map):
    for i in range(0, len(map)):
        map[i][0] = 1
    for i in range(0, len(map[0])):
        map[0][i] = 1
    for i in range(1, len(map)):
        for j in range(1, len(map[0])):
            map[i][j] = map[i - 1][j] + map[i][j - 1]
    return map[len(map) - 1][len(map[0]) - 1]
