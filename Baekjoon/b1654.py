import sys


def search(mid):
    cnt = 0
    for i in range(len(lancables)):
        cnt += lancables[i] // mid
    return cnt


k, n = map(int, sys.stdin.readline().split())

lancables = []
for _ in range(k):
    lancables.append(int(sys.stdin.readline()))

left, right, ans = 0, max(lancables), 0
while left <= right:
    mid = (left + right) // 2
    if mid == 0:
        ans = 1
        break

    cnt = search(mid)
    if cnt >= n:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)