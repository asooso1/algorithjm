def solution(d, budget):
    answer = 0
    total =0
    d.sort()
    for money in d :
        if total + money <= budget:
            total += money
            answer += 1
        else :
            continue
    return answer
print(solution([1,3,2,5,4],9))
