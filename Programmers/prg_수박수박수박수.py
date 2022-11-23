def solution(n):
    answer = ''
    for i in range(1,n+1):
        if not i % 2:
            answer += '박'
        else :
            answer += '수'
    return answer
print(solution(3))
print(solution(4))