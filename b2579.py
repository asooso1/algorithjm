import sys
sys.stdin = open('b2579.txt')

N = int(input())
floors = [int(input()) for _ in range(N)]
floors.reverse()

# dp = [(0, 0, 0) for _ in range(N)]
dp = [0] * (N + 1)


# dp[1] = (floors[0] + floors[1], floors[0)

for i in range(1, N - 1):
    dp[i] = dp[i - 1] + max(floors[i],floors[i + 1])
    
    # if i % 3 == 0:
    #     dp[i] = (dp[i - 1][0]
    # if i % 3 == 0:
    #     dp[i] = (dp[i - 1][0], dp[i - 1][1] + floors[i], dp[i - 1][2]+floors[i])
    # elif i % 3 == 1:
    #     dp[i] = (dp[i - 1][0] + floors[i], dp[i - 1][1], dp[i - 1][2]+floors[i])
    # elif i % 3 == 2:
    #     dp[i] = (dp[i - 1][0]+floors[i], dp[i - 1][1] + floors[i], dp[i - 1][2])
    

print(dp)