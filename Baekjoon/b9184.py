import sys
sys.stdin = open('b9184.txt')

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif dp[a][b][c]:
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] =  w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]
    
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
while True:
    A, B, C = map(int, input().split())
    
    if A == -1 and B == -1 and C == -1:
        break
    result = w(A, B, C)

    print(f'w({A}, {B}, {C}) = {result}')
    # print('%d, %d, %d' %(A,B,C))