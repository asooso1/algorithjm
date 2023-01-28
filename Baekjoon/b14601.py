import sys
sys.stdin = open('b14601.txt')

k = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())

num = 0
length = pow(2, k)
map = [[0] * length for _ in range(length)]
map[x - 1][y - 1] = -1

def checkHole(x, y, len):
    for i in range(x, x + len):
        for j in range(y, y + len):
            if map[i][j] != 0:
                return False

    return True

def tromino(x, y, len):
    global num
    num += 1
    halfLen = len // 2
    if (checkHole(x, y, halfLen)):
        map[x + halfLen - 1][y + halfLen - 1] = num
    if (checkHole(x, y + halfLen, halfLen)):
        map[x + halfLen - 1][y + halfLen] = num
    if (checkHole(x + halfLen, y, halfLen)):
        map[x + halfLen][y + halfLen - 1] = num
    if (checkHole(x + halfLen, y + halfLen, halfLen)):
        map[x + halfLen][y + halfLen] = num
    if halfLen == 2:
        return

    tromino(x, y, halfLen)
    tromino(x, y +  halfLen, halfLen)
    tromino(x + halfLen, y, halfLen)
    tromino(x + halfLen, y + halfLen, halfLen)

tromino(0, 0, length)

for i in range(length):
    for j in range(length):
        print(map[i][j], end=' ')
    print()