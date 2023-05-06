import sys
sys.stdin = open('b10989.txt', 'r')

N = int(sys.stdin.readline().rstrip())
# 카운팅정렬 array
nums = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    nums[num] += 1

cnt = 0

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)
            cnt += 1
    if cnt == N:
        break