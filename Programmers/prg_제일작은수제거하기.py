def solution(arr):
    answer = []
    min_num = min(arr)
    arr.remove(min(arr))
    answer = arr
    if len(answer) > 0 :
        return answer
    else :
        return [-1]

print(solution([4,3,2,1]))
print(solution([10]))