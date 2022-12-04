import sys
sys.stdin = open('1945_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    answer = [0, 0, 0, 0, 0]
    while True:
        if not N % 2 :
            N //= 2
            answer[0] += 1
        elif not N % 3 :
            N //= 3
            answer[1] += 1
        elif not N % 5 :
            N //= 5
            answer[2] += 1
        elif not N % 7 :
            N //= 7
            answer[3] += 1
        elif not N % 11 :
            N //= 11
            answer[4] += 1
        else :
            break
    print(f'#{test_case}',end=' ')
    print(*answer)