for tc in range(1, int(input())+1):
    N = int(input())
    trees = list(map(int,input().split()))
    trees.sort()
    result = []
    toggle = 1
    while len(trees):   # 정렬하고 가장 큰 수를 기준으로 내림차순으로 왼쪽, 오른쪽에 배치
        if toggle:
            result.append(trees.pop(-1))
            toggle = 0
        else:
            result.insert(0,trees.pop(-1))
            toggle = 1
    max_diff = 0
    for i in range(len(result)-1):  # 인접한 두 통나무의 차이의 최댓값 찾기
        if abs(result[i+1] - result[i]) > max_diff:
            max_diff = abs(result[i+1] - result[i])
    
    print(max_diff)