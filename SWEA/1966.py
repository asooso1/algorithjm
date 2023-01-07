T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    list_num = list(map(int,input().split()))
    list_num.sort()

    print(f'#{test_case} ',end='')
    print(*list_num)