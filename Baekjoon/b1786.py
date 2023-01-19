import sys
sys.stdin = open('b1786.txt')

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
def make_pi():
    pi = [0 for i in range(0, len(P))]

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]

        if (P[i] == P[j]):
            j += 1
            pi[i] = j
    return pi

n_pi = make_pi()
result = []
count = 0

j = 0
for i in range(0, len(T)):

    while j > 0 and T[i] != P[j]:
        j = n_pi[j - 1]

    if T[i] == P[j]:
        if j == (len(P) - 1):
            result.append(i - len(P) + 2)
            count += 1
            j = n_pi[j]
        else:
            j += 1

print(count)
for element in result:
    print(element)