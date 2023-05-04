import sys
sys.stdin = open('b1300.txt', 'r')

N = int(input())
K = int(input())

# 이분탐색
def bin_search(target, start, end):
    while start <= end:
        middle = (start + end) // 2
        cnt = 0

        for i in range(1, N+1):
            cnt += min(middle//i, N)

        if cnt >= target:
            end = middle - 1
        else:
            start = middle + 1
    return start

print(bin_search(K, 1, N*N))