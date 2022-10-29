def solution(n, lost, reserve):
    answer = n-len(lost)
    
    lost.sort()
    reserve.sort()
    real_lost = []
    for idx in range(len(lost)):
        if lost[idx] in reserve:
            answer += 1
            reserve.remove(lost[idx])
        else :
            real_lost.append(lost[idx])
    for student in range(len(real_lost)):
        if real_lost[student]-1 in reserve :
            answer += 1
            reserve.remove(real_lost[student]-1)
        elif real_lost[student]+1 in reserve :
            answer += 1
            reserve.remove(real_lost[student]+1)
        else :
            pass
            
    return answer

# 하나의 반복문에서 앞사람이 있는지 확인, 있으면 reserve에서 요소 제거, 없으면 뒷사람 있는지 확인, 있으면 요소 제거, 중요한건 잃어버렸는데 여분체육복 있는사람들이 있음. 최초에 확인하고 새로운 리스트 생성
