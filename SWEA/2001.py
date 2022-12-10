T = int(input())
for test_case in range(T):
    list_fly = []
    N,M = map(int,input().split(' '))
    for idx in range(N):
        list_fly.append(list(map(int,input().split(' '))))  # 이중 리스트 생성
        max_sum = 0             # 최댓값 비교를 위한 변수
        max_sum_temp = 0        # 임시 합 저장변수

    for line in range(N-M+1):                               # 행(line) 열(row) 컨트롤하는 이중 for
        for row in range(N-M+1):
            for i in range(M):                              # 좌상단의 기준점을 시작으로 우측,하단 M만큼의 value 합 임시저장
                max_sum_temp += sum(list_fly[line+i][row:row+M])
            if max_sum_temp > max_sum :                     # 임시저장값이 기존 최댓값보다 높으면 최댓값 변경
                max_sum = max_sum_temp
            max_sum_temp = 0                                # 임시저장변수 초기화
            
    print(f'#{test_case+1} {max_sum}')