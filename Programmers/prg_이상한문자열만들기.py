def solution(s):
    answer = ''
    char_count = 0
    for idx in range(len(s)):
        if s[idx] == ' ':
            answer += s[idx]
            char_count = 0
        elif char_count % 2 == 0:
            answer += s[idx].upper()
            char_count += 1
        elif char_count % 2 == 1:
            answer += s[idx].lower()
            char_count += 1
        else :
            pass
    
    return answer

print(solution("try hello world")) # => "TrY HeLlO WoRlD"