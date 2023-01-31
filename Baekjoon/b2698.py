import sys
sys.stdin = open('b2698.txt')

T = int(input())
for tc in range(T):
    n, k = map(int, int(sys.stdin.readline().split()))
    f = [0] * (n + 1)
    
    