
T = int(input())
for test_case in range(1,T+1):
    N, k = map(int,input().split(' '))
    answer = 0
    square = []

    square.append([0]*(N+2))
    for i in range(N):
        line = list(map(int,input().split()))
        line.insert(0,0)
        line.append(0)
        square.append(line)
    square.append([0]*(N+2))

    for j in range(1,N+2):
        for m in range(1,N+2):
            if square[j][m:m+k].count(1) == k and square[j][m+k] != 1 and square[j][m-1] != 1:  #가로
                answer += 1

    rotate_square = []
    for a in range(0,N+2):
        line = []
        for b in range(0,N+2):
            line.append(square[b][a])
        rotate_square.append(line)
    
    for j in range(1,N+2):
        for m in range(1,N+2):
            if rotate_square[j][m:m+k].count(1) == k and rotate_square[j][m+k] != 1 and rotate_square[j][m-1] != 1:  #세로
                answer += 1
    print(f'#{test_case} {answer}')