def average_no_min_max(list_num):
    pass
    answer = 0
    list_num.remove(max(list_num))
    list_num.remove(min(list_num))
    answer = round(sum(list_num)/8)
    return answer

T = int(input())
for test_case in range(1,T+1):
    list_testcase = list(map(int,input().split()))
    print(f'#{test_case} {average_no_min_max(list_testcase)}')