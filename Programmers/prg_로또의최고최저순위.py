def solution(lottos, win_nums):
    answer = []
    max_score = 0
    min_score = 0
    for number in lottos :
        if number == 0:
            max_score += 1
        else :
            if number in win_nums:
                max_score += 1
                min_score += 1
    if max_score <= 1:
        answer.append(6)
        answer.append(6)
    elif min_score <= 1:
        answer.append(7-max_score)
        answer.append(6)
    else :
        answer.append(7-max_score)
        answer.append(7-min_score)
            
    return answer

# 모르는 번호를 0으로 하고 0이 다 맞았을때 max_score, 다 틀렸을 때 min_score로 answer에 저장