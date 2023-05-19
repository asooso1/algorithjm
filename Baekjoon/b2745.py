import sys
sys.stdin = open('2745.txt')

answer = 0
N, B = sys.stdin.readline().split()
B = int(B)

for i in range(len(N)):
    ascii_num = ord(N[-(i + 1)])
    if ascii_num >= 65 and ascii_num <= 90:
        answer += (ascii_num - 65 + 10) * (B ** i)
    else:
        answer += int(N[-(i + 1)]) * (B ** i)
print(answer)