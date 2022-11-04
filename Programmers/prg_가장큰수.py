# 가장 큰 수
def solution(numbers):
    answer = ''
    check_str =''
    for number in numbers:
        check_str += str(number)
    check_list = list(map(int,check_str))           # string int_list화
    check_list = list(reversed(sorted(check_list))) # 내림차순정렬
    for num in check_list:
        answer += str(num)
    return answer
print(solution([3, 30, 34, 5, 9]))