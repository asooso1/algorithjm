def solution(a, b):
    answer = 1234567890
    total = 0
    for idx in range(len(a)):
        total += a[idx]*b[idx]
    answer = total
    return answer
print(solution([1,2,3,4],[-3,-1,0,2]))