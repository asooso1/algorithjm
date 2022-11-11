def solution(left, right):
    answer = 0
    for number in range(left,right+1):
        div_count = 0
        for i in range(1,number+1):
            if not number % i:
                div_count += 1
        if not div_count % 2:
            answer += number
        else :
            answer -= number
    return answer

print(solution(13,17))