N, K = map(int, input().split())
numbers = [n for n in range(1,N+1)]
answer = []
stack_pt = K-1  # 초기값
while numbers:
    answer.append(numbers[stack_pt])
    if stack_pt >= len(numbers):
        stack_pt %= len(numbers)
    else:
        stack_pt += K
    print(answer)