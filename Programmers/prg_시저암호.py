def solution(s, n):
    answer = ''
    for char in s:
        if char.islower():
            if ord(char) + n > 122:
                answer += chr(((ord(char)+n)%123)+97)
            else :
                answer += chr(ord(char)+n)
        elif char.isupper():
            if ord(char) + n > 90:
                answer += chr(((ord(char)+n)%91)+65)
            else :
                answer += chr(ord(char)+n)
        else :
            answer += char
    return answer
solution('z',1)
solution('a B z',4)
solution('AB',1)