def solution(s):
    answer = 0
    ans_str = ''
    start_char = ['z', 'o', 't', 'f', 's', 'e', 'n']
    idx = 0
    while idx < len(s):
        if s[idx] in start_char :
            if s[idx] == 'z':
                ans_str += '0'
                idx += 4
            elif s[idx] == 'o':
                ans_str += '1'
                idx += 3
            elif s[idx:idx+2] == 'tw':
                ans_str += '2'
                idx += 3
            elif s[idx:idx+2] == 'th':
                ans_str += '3'
                idx += 5
            elif s[idx:idx+2] == 'fo':
                ans_str += '4'
                idx += 4
            elif s[idx:idx+2] == 'fi':
                ans_str += '5'
                idx += 4
            elif s[idx:idx+2] == 'si':
                ans_str += '6'
                idx += 3
            elif s[idx:idx+2] == 'se':
                ans_str += '7'
                idx += 5
            elif s[idx] == 'e':
                ans_str += '8'
                idx += 5
            elif s[idx] == 'n':
                ans_str += '9'
                idx += 4
            else :
                pass
        else :
            ans_str += s[idx]
            idx += 1
    answer = int(ans_str)
    return answer


# 문자열의 시작 char를 비교해서 숫자로 변환하고 인덱스를 다음 숫자 or 새로운 숫자문자열로 이동