def solution(arr):
    answer = []
    answer.append(arr[0])
    j = 0
    # i = 0                                         arr 내부에서 비교하면 효율성이 떨어지므로 직전에 answer list에 넣었는지 확인하고 없으면 추가하는 알고리즘으로 변경
    # while i < len(arr)-1:
    #     if arr[i] == arr[i+1]:
    #         arr.pop(i)
    #     else :
    #         i += 1
    for i in range(len(arr)):
        if arr[i] != answer[j]:
            answer.append(arr[i])
            j +=1
        else :
            pass
    return answer
print(solution([1,1,3,3,0,1,1]))