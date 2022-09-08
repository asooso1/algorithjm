import sys
sys.stdin = open('b14888.txt')

# + - * //

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, input().split()))

max_limit = -(10 ** 9)
min_limit = 10 ** 9
visited = [0] * N

def search(s, k):
    global min_limit, max_limit
    if k == N:
        if s < min_limit:
            min_limit = s
        if s > max_limit:
            max_limit = s
        return

    for i in range(4):
        if operator[i] == 0:
            continue
        operator[i] -= 1
        if i == 0:
            search(s + A[k], k + 1)
        elif i == 1:
            search(s - A[k], k + 1)
        elif i == 2:
            search(s * A[k], k + 1)
        elif i == 3:
            if s >= 0:
                search(s // A[k], k + 1)
            else:
                search(-(abs(s) // A[k]), k + 1)
        operator[i] += 1

search(A[0], 1)
print(max_limit, min_limit)