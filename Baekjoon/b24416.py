# pypy3로 제출해야 초과나지않는다
import sys
sys.stdin = open('b24416.txt')

N = int(input())
cnt_rec = 1
cnt_dp = 0
def fibonacci(n):
    global cnt_rec
    cnt_rec += 1
    if n == 1 or n == 2:
        cnt_rec -= 1
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

def fib_dp(n):
    global cnt_dp
    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        cnt_dp += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

f = [0] * 41

fibonacci(N)
fib_dp(N)
print(cnt_rec, cnt_dp)
