def solution(answers):
    answer = []
    list_1 = [1,2,3,4,5]
    list_2 = [2,1,2,3,2,4,2,5]
    list_3 = [3,3,1,1,2,2,4,4,5,5]      # 각 사람의 찍는 방식 저장
    ans_list = [0, 0, 0]                # 맞춘 갯수 저장 list
    for idx,ans in enumerate(answers) :
        if ans == list_1[idx % 5]:
            ans_list[0] += 1
        else :
            pass
        if ans == list_2[idx % 8]:
            ans_list[1] += 1
        else :
            pass
        if ans == list_3[idx % 10]:
            ans_list[2] += 1
        else :
            pass
        
        
    if max(ans_list) == ans_list[0]:
        answer.append(1)
    else :
        pass
    if max(ans_list) == ans_list[1]:
        answer.append(2)
    else :
        pass
    if max(ans_list) == ans_list[2]:
        answer.append(3)
    else :
        pass
    return answer

a = solution([1,3,2,4,2])
print(a)