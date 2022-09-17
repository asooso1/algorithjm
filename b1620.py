import sys
sys.stdin = open('b1620.txt')

N, M = map(int, input().split())
pokemons = [sys.stdin.readline().rstrip() for _ in range(N)]
dict_pokemons = {}

# # ASCII 코드 사용 => 시간초과
# for i in range(1, N + 1):
#     dict_pokemons[pokemons[i - 1]] = i

# for _ in range(M):
#     question = sys.stdin.readline().rstrip()
#     if ord(question[0]) >= 65 and ord(question[0]) <= 90:
#         print(dict_pokemons[question])
#     else:
#         for k, v in dict_pokemons.items():
#             if v == int(question):
#                 print(k)

# dict만 사용
for i in range(1, N + 1):
    dict_pokemons[pokemons[i - 1]] = str(i)
    dict_pokemons[str(i)] = pokemons[i - 1]

for _ in range(M):
    question = sys.stdin.readline().rstrip()
    print(dict_pokemons[question])