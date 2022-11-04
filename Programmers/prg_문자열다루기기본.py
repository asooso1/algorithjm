def solution(s):
    answer = True
    if not(len(s) == 4 or len(s) == 6):
        return False
    else :
        if s.isdecimal():
            return True
        else :
            return False
