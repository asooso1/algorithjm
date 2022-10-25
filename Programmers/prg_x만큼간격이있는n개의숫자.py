def solution(x, n):
    answer = []
    if x > 0:
        for i in range(x,(x*n)+1,x):
            answer.append(i)
    elif x < 0 :
        for i in range(x,(x*n)-1,x):
            answer.append(i)
    else :
        answer = [0] * n
    return answer

# x가 0일때 주의하기.