def solution(n):
    answer = 0
    string = str(n)
    for char in string:
        answer += int(char)
    return answer

print(solution(3456))