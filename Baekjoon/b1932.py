import sys
sys.stdin = open('b1932.txt')

N = int(input())
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            tri[i][j] += tri[i - 1][j]
        elif j == i:
            tri[i][j] += tri[i - 1][j - 1]
        else:
            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])
print(max(tri[-1]))