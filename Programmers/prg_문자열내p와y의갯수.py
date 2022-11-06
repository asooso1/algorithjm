def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    for i in range(len(s)):
        if s[i].isupper():
            if s[i].lower() == 'p':
                p_count += 1
            elif s[i].lower() == 'y':
                y_count += 1
        else :
            if s[i].lower() == 'p':
                p_count += 1
            elif s[i].lower() == 'y':
                y_count += 1
    if p_count == y_count :
        return True
    else :
        return False

print(solution('pPoooyY'))
print(solution('Pyy'))