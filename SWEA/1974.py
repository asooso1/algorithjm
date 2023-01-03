import sys
sys.stdin = open('1974_input.txt','r')
T = int(input())
for test_case in range(1, T+1):
    answer = 1
    sudoku = []
    for idx in range(9):
        sudoku.append(list(map(int,input().split())))

    for i in range(9):  # 가로 세로 검증
        line_sum = 0
        row_sum = 0
        for j in range(9):
            line_sum += sudoku[i][j]
            row_sum += sudoku[j][i]
        if line_sum != 45 or row_sum != 45 :
            answer = 0
            break
        else :
            continue
    
    if answer:
        for n in range(0,9,3):  # 사각형 검증
            square1_sum = 0
            square2_sum = 0
            square3_sum = 0
            for m in range(3):
                square1_sum += sudoku[n][m] + sudoku[n+1][m] + sudoku[n+2][m]
                square2_sum += sudoku[n][m] + sudoku[n+1][m] + sudoku[n+2][m]
                square3_sum += sudoku[n][m] + sudoku[n+1][m] + sudoku[n+2][m]
            if square1_sum != 45 or square2_sum != 45 or square3_sum != 45:
                answer = 0
                break
            else :
                continue
            
    print(f'#{test_case} {answer}')