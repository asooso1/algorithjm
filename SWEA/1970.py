T = int(input())
for test_case in range(1,T+1):
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer_list = [0, 0, 0, 0, 0, 0, 0, 0]
    N = int(input())
    for i in range(8):
        answer_list[i] += N // money_list[i]
        N %= money_list[i]
    print(f'#{test_case}')
    print(*answer_list)