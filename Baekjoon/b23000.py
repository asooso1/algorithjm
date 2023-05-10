import sys
sys.stdin = open('b23000.txt')

N = int(sys.stdin.readline())
machines = list(map(int, sys.stdin.readline().split()))

machines.sort()

totals = []

# 홀수개의 머신이라면 최대 근손실이 발생할 머신은 무조건 하나만 사용해야 최소를 충족
if N % 2 == 1:
    totals.append(machines.pop())
    

for i in range(len(machines) // 2):
    totals.append(machines[i] + machines[len(machines) - 1 - i])
    

print(max(totals))

