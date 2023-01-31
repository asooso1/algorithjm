import sys
sys.stdin = open('b15650.txt')

N, M = map(int, input().split())
P = []
v = [0] * (N + 1)
def search(k):
    if len(P) == M:
        print(" ".join(map(str, P)))
        return
    for i in range(k, N + 1):
        if v[i] == 1:
            continue
        v[i] = 1
        P.append(i)
        search(i)
        P.pop()
        v[i] = 0
        
search(1)