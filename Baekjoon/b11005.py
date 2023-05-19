import sys
sys.stdin = open('11005.txt')

answer = ''
N, B = map(int, sys.stdin.readline().split())

while N > 0:
    num = N % B
    if num >= 10:
        num = chr(num + 65 - 10)
    else:
        num = str(num)
    answer = num + answer
    N //= B
print(answer)