def solution(absolutes, signs):
    answer = 0
    def plus_and_minus(num,bool_sign):
        if bool_sign :
            return num
        else :
            return -num
    for i in range(len(signs)):
        answer += plus_and_minus(absolutes[i],signs[i])
    return answer
print(solution([4,7,12],[True,False,True]))
print(solution([1,2,3],[False,False,True]))