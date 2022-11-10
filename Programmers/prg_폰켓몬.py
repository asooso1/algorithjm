def solution(nums):
    answer = 0
    nums_set = set(nums)
    if len(nums)//2 <= len(nums_set):
        return len(nums)//2
    else :
        return len(nums_set)
    

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))