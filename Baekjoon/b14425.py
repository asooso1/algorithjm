import sys
sys.stdin = open('b14425.txt')

N, M = map(int, input().split())
S = [input() for _ in range(N)]
questions = [input() for _ in range(M)]

# dict => set 도 동일한 시간복잡도를 가진다. (해쉬테이블로 구성되어있기 떄문)
dict_S = {}
answer = 0

for string in S:
    dict_S[string] = True

for q in questions:
    if q in dict_S:
        answer += 1

print(answer)

