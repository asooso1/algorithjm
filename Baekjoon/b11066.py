import sys
sys.stdin = open('b11066.txt')

T = int(sys.stdin.readline())

for tc in range(T):
    K = int(sys.stdin.readline())
    files = [0] + list(map(int, sys.stdin.readline().split()))
    S = [0 for _ in range(K+1)]

    for i in range(1, K+1):
        S[i] = S[i-1] + files[i]
    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]

    for i in range(2, K+1):
        for j in range(1, K+2-i):
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1] - S[j-1])
 
    print(dp[1][K])