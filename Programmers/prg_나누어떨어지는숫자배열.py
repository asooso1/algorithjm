def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if not arr[i] % divisor:
            answer.append(arr[i])
    
    answer.sort()
    if not len(answer):
        return [-1]
    else :
        return answer

print(solution([5,9,7,10],5))
print(solution([2,36,1,3],1))