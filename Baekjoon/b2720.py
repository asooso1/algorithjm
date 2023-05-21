import sys
sys.stdin = open('b2720.txt')

cents = {0 : 25, 1 : 10, 2 : 5, 3 : 1}
T = int(input())
for tc in range(T):
    C = int(input())

    result = [0] * 4
    for i in range(4):
        result[i] = C // cents[i]
        C = C % cents[i]

    print(*result, sep=" ")