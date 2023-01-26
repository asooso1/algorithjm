import sys
sys.stdin = open('b2447.txt')

# N = int(sys.stdin.readline())
# for i in range(N):
#     for j in range(N):
#         if ((i + 1) % 3 == 2 and (j + 1) % 3 == 2) or ():
#             print(' ', end="")
#         else:
#             print('*', end="")
#     print()
def draw_stars(n):
    if n==1:
        return ['*']

    Stars=draw_stars(n//3)
    L=[]

    for star in Stars:
        L.append(star*3)
    for star in Stars:
        L.append(star+' '*(n//3)+star)
    for star in Stars:
        L.append(star*3)

    return L

N=int(input())
print('\n'.join(draw_stars(N)))