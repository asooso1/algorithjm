def solution(s):
    temp_list = s[2:-2].split('},{')
    temp_list2 = []
    arr = []
    for i in range(len(temp_list)):
        temp_list2.append(list(map(int,temp_list[i].split(','))))
    for i in range(len(temp_list2)):
        for j in range(0,len(temp_list2)):
            if len(temp_list2[j]) == i+1:
                arr.append(temp_list2[j])

    temp_dict = dict(enumerate(arr))
    answer = [temp_dict[0][0]]
    for key,string in temp_dict.items():
        if key != len(arr)-1:
            a = set(string)
            b = set(temp_dict[key+1])
            answer.append((b-a).pop())
    return answer
#     s = s.replace('{','',1000000).replace('}','',1000000)
# replace 사용해서 리팩토링해보기
    
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))