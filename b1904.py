import sys
sys.stdin = open('b1904.txt')

N = int(input())
v = [0] * N
# S = set()
# 00 or 1
# def search(idx):

f = [0] * N
f[0] = 1
if N > 1:
    f[1] = 2
    for i in range(2, N):
        f[i] = (f[i-1] + f[i-2]) % 15746
print(f[N - 1])