import sys
sys.stdin = open('b14889.txt')

N = int(input())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
v = [0] * N
min_abil = 100 * N

def team_search(k, team):
    global min_abil
    if len(team) * 2 == N:
        sA = 0
        sB = 0
        for i in range(N - 1):
            for j in range(i + 1, N):
                if v[i] and v[j]:
                    sA += S[i][j] + S[j][i]
                elif not v[i] and not v[j]:
                    sB += S[i][j] + S[j][i]
        min_abil = min(min_abil, abs(sA - sB))
        return
    
    for i in range(k, N):
        if not v[i]:
            v[i] = 1
            team.append(i)
            team_search(i, team)
            v[i] = 0
            team.pop()

team_search(0, [])
print(min_abil)