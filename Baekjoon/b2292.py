import sys
sys.stdin = open('b2292.txt')

N = int(input())


gap = 6
max_honeycomb = 1
cnt = 1
while N > max_honeycomb:
    max_honeycomb += gap
    gap += 6
    cnt += 1
print(cnt)
