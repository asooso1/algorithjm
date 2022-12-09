# T = int(input())
    # for test_case in range(1,T+1):
    # print(f'#{test_case} {cnt*N}')

def solution(N):
    num_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cnt = 0
    while num_count.count(0):
        cnt += 1
        num = cnt * N
        for char in str(num):
            num_count[int(char)] += 1
    print(N*cnt)

solution(1)
solution(2)
solution(11)
solution(1295)
solution(1692)

