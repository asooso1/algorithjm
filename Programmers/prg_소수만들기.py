def solution(nums):
    answer = 0
    total_list = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                total_list.append(nums[i]+nums[j]+nums[k])
    for num in total_list:
        count = 0
        for a in range(2,num+1):
            if not num % a:
                count += 1
        if count == 1:
            answer += 1
                
    return answer
print(solution([1,2,7,6,4]))
print(solution([1,2,3,4]))