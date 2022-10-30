def solution(n, arr1, arr2):
    answer = []
    arr_sum = []
    line_str = ''
    
    for i in range(len(arr1)):
        arr_sum.append(arr1[i]|arr2[i])
        
    for num in arr_sum:
        for idx in range(n):
            if num % 2 :
                line_str = '#' + line_str
            else :
                line_str = ' ' + line_str
            num //= 2
        answer.append(line_str)
        line_str = ''
        
    return answer


print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
