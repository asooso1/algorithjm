import collections
N = int(input())

deck = collections.deque([n for n in range(N,0, -1)]) # 최초 카드 덱
i = 1
while len(deck)!= 1:    # 1장이 될때 까지 진행
    if i % 2:   # 카드를 버리는것과 제일 위의 카드를 아래로 버리는 것을 번갈아가면서 진행
        deck.pop()  # 맨 위카드 버리기
        i += 1
    elif not i % 2: # 맨위 카드 제일 아래로 이동
        deck.rotate(1) # 오른쪽으로 회전
        i += 1
print(deck[0])
