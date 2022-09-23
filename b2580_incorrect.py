# 다시풀기
import sys
sys.stdin = open('b2580.txt')

puzzle = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

def find_zero(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                return (i ,j)
    return None
def sudoku_check(n, pos):
    x = pos[0]
    y = pos[1]
    # 정사각형 확인
    
    for i in range((x // 3) * 3, (x // 3) * 3 + 3):
        for j in range((y // 3) * 3, (y // 3) + 3):
            if puzzle[i][j] == n:
                return False
    # 가로줄 확인
    for i in range(0, 9):
        if puzzle[x][i] == n:
            return False
    
    # 세로줄 확인
    for i in range(0, 9):
        if puzzle[i][y] == n:
            return False
    return True

def search():
    find_pos = find_zero(puzzle)
    if not find_pos:
        return True
    
    for n in range(1, 10):
        if sudoku_check(n, find_pos):
            puzzle[find_pos[0]][find_pos[1]] = n
            if search():
                return True
            puzzle[find_pos[0]][find_pos[1]] = 0
    return False
            
search()
for i in range(9):
    for j in range(9):
        print(puzzle[i][j], end=" ")
    print()


