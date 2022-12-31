import sys
sys.stdin = open('1940_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    now_accel = 0
    total = 0
    for case in range(N):
        try :
            command, input_accel = map(int,input().split())
        except ValueError:
            input_accel = 0
        if not command:
            total += now_accel
        elif command == 1:
            now_accel += input_accel
            total += now_accel
        elif command == 2:
            now_accel -= input_accel
            if now_accel < 0:
                now_accel = 0
            total += now_accel
        else :
            continue
    print(f'#{test_case} {total}')