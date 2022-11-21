def solution(strings, n):
    answer = []
    new_strings = []
    for idx in range(len(strings)):
        strings[idx] = strings[idx][n] + strings[idx]
        new_strings.append(strings[idx])
    new_strings.sort()
    for string in new_strings:
        answer.append(string[1:])
    return answer
print(solution(["sun", "bed", "car"],1))