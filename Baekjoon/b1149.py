# import sys
# sys.stdin = open('b1149.txt')

# N = int(input())
# RGBs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# f = [0] * N
# color = -1   # 색 번호
# min_num = 2000  # 초기 비교값
# for i in range(3):
#     for j in range(3):
#         if i != j and min_num > RGBs[0][i] + RGBs[1][j]:
#             min_num = RGBs[0][i] + RGBs[1][j]
#             color = j            
# f[1] = min_num
# # print(f[1])
# if N >= 2:
#     for i in range(2, N):
#         # RGBs[i][color] = 1001
#         # f[i] = f[i - 1] + min(RGBs[i])
#         t = RGBs[i][0]
#         for j in range(3):
#             if j != color and t > RGBs[i][j]:
#                 t = RGBs[i][j]
#                 color = j
#         f[i] = f[i - 1] + t
                
            
# print(f[N - 1])
# print(f)

import sys
sys.stdin = open('b1149.txt')

N = int(input())
colors = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    colors[i][0] += min(colors[i - 1][1], colors[i - 1][2])
    colors[i][1] += min(colors[i - 1][0], colors[i - 1][2])
    colors[i][2] += min(colors[i - 1][0], colors[i - 1][1])

print(min(colors[-1]))