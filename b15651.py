import sys
sys.stdin = open('b15651.txt')

N, M = map(int, input().split())
S = []

def search():
    if len(S) == M:
        print(" ".join(map(str, S)))
        return
    for i in range(1, N + 1):
        S.append(i)
        search()
        S.pop()

search()