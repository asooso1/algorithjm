import sys
sys.stdin = open('b9461.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    if N < 3:
        print(1)
        continue
    f = [0] * N
    f[0] = 1
    f[1] = 1
    f[2] = 1
    for i in range(3, N):
        f[i] = f[i-2] + f[i-3]
    print(f[N - 1])