T = int(input())
for test_case in range(1,T+1):
    hour1, min1, hour2, min2 = map(int,input().split())
    hour = (hour1 + hour2) % 12
    if min1 + min2 >= 60:
        hour += 1
        min = (min1 + min2) % 60

    else :
        min = min1 + min2

    print(f'#{test_case} {hour} {min}')