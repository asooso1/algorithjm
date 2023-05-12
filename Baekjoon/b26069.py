import sys
sys.stdin = open('b26069.txt')

n = int(sys.stdin.readline())
dance = {'ChongChong'}

for i in range(1, n+1):
    a, b = sys.stdin.readline().split()

    if a in dance:
        dance.add(b)

    if b in dance:
        dance.add(a)

print(len(dance))