def solution(n, m):
    answer = []
    min_num = m
    
    if n > m :
        for i in range(m,0,-1):
            if n % i == 0 and m % i == 0 :
                answer.append(i)
                break
        while True:
            if min_num % n == 0 and min_num % m == 0:
                answer.append(min_num)
                break
            else :
                min_num += 1    
    elif n < m :
        for i in range(n,0,-1):
            if n % i == 0 and m % i == 0 :
                answer.append(i)
                break
        while True:
            if min_num % n == 0 and min_num % m == 0:
                answer.append(min_num)
                break
            else :
                min_num += 1
    else :
        return [n,n]
    return answer

print(solution(3,12))
print(solution(2,5))