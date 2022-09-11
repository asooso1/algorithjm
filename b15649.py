# 다시풀기

import sys
sys.stdin = open('b15649.txt')

# n, m = map(int, input().split())
# result = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        print(s)
        dfs()
        s.pop()
        print(s)
        # print(visited)
        visited[i] = False
            

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()