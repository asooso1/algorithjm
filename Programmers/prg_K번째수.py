# K 번째 수
arr = [1, 5, 2, 6, 3, 7, 4]
com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
def solution(array, commands):
    answer = []
    for list_idx in commands:
        i = list_idx[0]-1
        j = list_idx[1]
        k = list_idx[2]-1
        list_check = array[i:j]
        list_check = sorted(list_check)
        answer.append(list_check[k])
    return answer
print(solution(arr,com))