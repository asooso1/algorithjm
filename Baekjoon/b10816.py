import sys
sys.stdin = open("b10816.txt")

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
questions = list(map(int, sys.stdin.readline().split()))
answer = [0] * M


# dict
dict_cards = {}
for i in range(N):
    if dict_cards.get(cards[i]):
        dict_cards[cards[i]] += 1
    else:
        dict_cards[cards[i]] = 1

for q in questions:
    if q in dict_cards:
        print(dict_cards[q], end=" ")
    else:
        print('0', end=" ")

# # binary search => 실패
# cards.sort()
# def binary_search(arr, target, start, end):
#     while start <= end:
#         middle = (start + end) // 2
#         if arr[middle] == target:
#             arr.pop(middle)
#             return 1
#         elif arr[middle] < target:
#             start = middle + 1
#         else:
#             end = middle - 1
#     return 0

# for i in range(M):
#     ans = 0
#     flag = 1
#     while flag == 1:
#         flag = binary_search(cards, questions[i], 0, len(cards) - 1)
#         ans += flag
#     answer[i] += ans
# print(' '.join(str(s) for s in answer))
    
