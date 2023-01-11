import sys
sys.stdin = open('1204_input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    students = int(input())
    scores = list(map(int,input().split()))
    most_count = 0
    score = 0
    for i in range(101):
        if most_count <= scores.count(i):
            most_count = scores.count(i)
            score = i
    print(f'#{test_case} {score}')