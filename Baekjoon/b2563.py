import sys
sys.stdin = open('b2563.txt')

N = int(input())

area = [[0] * 100 for _ in range(100)]

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for p in range(x, x+10):
        for p2 in range(x, x+10):
            area[p][p2] = 1

answer = sum([sum(area[i]) for i in range(100)])
print(answer)