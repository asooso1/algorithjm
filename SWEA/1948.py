import sys
sys.stdin = open('1948_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    mon1, day1, mon2, day2 = map(int,input().split())
    day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    for i in range(mon1):
        day1 += day[i]
    for i in range(mon2):
        day2 += day[i]
    
    print(f'#{test_case} {day2-day1+1}')
