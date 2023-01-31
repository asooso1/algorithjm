import sys
sys.stdin = open('b15652.txt')

N, M = map(int, input().split())
S = []

def search(k):
    if len(S) == M:
        print(" ".join(map(str, S)))
        return
    for i in range(k, N + 1):
        S.append(i)
        search(i)
        S.pop()
search(1)