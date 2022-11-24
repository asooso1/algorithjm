def solution(participant, completion):
    answer = ''
    for person in participant :
        if person in completion :
            completion.remove(person)
        else :
            answer += person
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

# 답은 나오는데 효율성 체크 (아마 in 조건을 사용하는게 아니라 정렬해서 각 index 비교해야할듯.)
# 미완주자는 단 한명이라고 한다. *************

def solution(parti,comple):
    ans = ''
    parti.sort()
    comple.sort()
    set_parti = set(parti)
    set_comple = set(comple)
    print(set_comple)
    set_list = list(set_parti - set_comple)
    print(set_list)
    for idx in parti:
        if idx in set_list:
            ans += idx
        else :
            pass
    
    return ans
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    # for i in range(len(completion)) :
    #     if participant[i] == completion[i] :
    #         pass
    #     else :
    #         if participant[i+1] == completion[i]:
    #             return participant[i]
    #         else :
    #             pass


# 정답코드
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)) :
        if participant[i] == completion[i] :
            if i == len(completion)-1:
                return participant[i+1]
        else :
            if participant[i+1] == completion[i]:
                return participant[i]
solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]	)
solution(["leo", "kiki", "eden"],['eden','kiki'])