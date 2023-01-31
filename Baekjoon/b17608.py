import sys
N = int(input())
sticks = [int(sys.stdin.readline()) for _ in range(N)]
last = sticks.pop()
cnt = 1 # 최초에 보이는 가장 오른쪽 포함
while sticks:
    temp = sticks.pop()
    if temp > last:
        cnt += 1
        last = temp
print(cnt)