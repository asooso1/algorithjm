import sys
sys.stdin = open('p136797.txt')

numbers = list(map(int, (list(sys.stdin.readline().rstrip()))))
phone = []
for i in range(1, 11, 3):
    t = []
    for j in range(3):
        t.append(j+i)
    phone.append(t)
print(phone)