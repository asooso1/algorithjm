import sys
sys.stdin = open('b1912.txt')

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

# 그리디......?
# max_sum = (-1000) * n
# S = 0
# for i in range(n):
#     if nums[i] < 0 and S + nums[i] < 0:
#         S = 0
#         continue
#     S += nums[i]
#     max_sum = max(S, max_sum)
# if max_sum == (-1000) * n:
#     max_sum = max(nums)

# DP
f = [0] * n
f[0] = nums[0]
for i in range(1, n):
    f[i] = max(nums[i], f[i - 1] + nums[i])
print(max(f))