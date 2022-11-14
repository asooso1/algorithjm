def solution(s):
    answer = ''
    char_list = []
    for char in s :
        char_list.append(ord(char))
    char_list.sort()
    string = reversed(char_list)
    for char in string:
        answer += chr(char)
    return answer

print(solution('Zbcdefg'))