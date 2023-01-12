import sys
sys.stdin = open('1946_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    answer = []
    N = int(input())
    temp_string = ''
    for case in range(N):
        char, num = input().split()
        for i in range(int(num)):
            if len(temp_string) < 10:
                temp_string += char
            else :
                answer.append(temp_string)
                temp_string = ''
                temp_string += char
    if temp_string:
        answer.append(temp_string)
    print(f'#{test_case}')
    print(*answer,sep='\n')