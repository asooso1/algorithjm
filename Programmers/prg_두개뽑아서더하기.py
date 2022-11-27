def solution(numbers):
    answer = []
    set_num = set({})
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            set_num.add(numbers[i]+numbers[j])
    answer = list(set_num)
    answer.sort()
    
    return answer

print(solution([2, 1, 3, 4, 1]))