import sys
sys.stdin = open('b19532.txt', 'r')

a, b, c, d, e, f = map(int, input().split())

# 브루트포스
def calc():
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a * x + b * y == c and d * x + e * y == f:
                return (x, y)

answer = calc()
print(' '.join(map(str, answer)))


# 이차방정식 풀이
# def calc():
#     x = int((c * e - f * b) / (a * e - d * b))
#     y = int((c * d - f * a) / (b * d - e * a))
#     return (x, y)

# answer = calc()
# print(' '.join(map(str, answer)))