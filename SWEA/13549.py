import sys
sys.stdin = open('sw13549.txt', 'r')

T = int(sys.stdin.readline().rstrip())
for tc in range(1, T + 1):
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    print(f'#{tc} ')
