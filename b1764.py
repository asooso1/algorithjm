import sys
sys.stdin = open('b1764.txt', 'r')

N, M = map(int, input().split())
nHeard = [sys.stdin.readline().rstrip() for _ in range(N)]
nWatched = [sys.stdin.readline().rstrip() for _ in range(M)]
cnt = 0
result = []

# dict

# dict_nHeard = {}
# for i in range(N):
#     dict_nHeard[nHeard[i]] = 1

# for j in range(M):
#     if nWatched[j] in dict_nHeard:
#         cnt += 1
#         result.append(nWatched[j])
# result.sort()


# set
set_nHeard = set(nHeard)
set_nWatched = set(nWatched)

result = list(set_nHeard & set_nWatched)
result.sort()
cnt = len(result)

print(cnt)
print(*result, sep="\n")