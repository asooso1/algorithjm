import sys
sys.stdin = open('b2630.txt', 'r')

N = int(sys.stdin.readline())
color_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

def divide(x, y, N):
    color = color_paper[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != color_paper[i][j] :
                divide(x, y, N//2)
                divide(x, y+N//2, N//2)
                divide(x+N//2, y, N//2)
                divide(x+N//2, y+N//2, N//2)
                return
    if color == 0 :
        result.append(0)    
    else :
        result.append(1)


divide(0,0,N)
print(result.count(0))
print(result.count(1))