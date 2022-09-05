
import sys
sys.stdin = open("b10815.txt", "r")

# 이진탐색
# N = int(input())
# nums = list(map(int,sys.stdin.readline().split()))
# M = int(input())
# questions = list(map(int,sys.stdin.readline().split()))
# answer = ''
# nums.sort()


# def binary_search(arr, target, s, e):
#     while s <= e:
#         m = (s + e) // 2
#         if arr[m] == target:
#             return m
#         elif arr[m] > target:
#             e = m - 1
#         else:
#             s = m + 1
#     return None

# for q in questions:
#     if binary_search(nums, q, 0, N - 1) is None:
#         print('0', end=' ')
#     else:
#         print('1', end=' ')
        
# # print(answer.rstrip())
# # rstrip 하면 시간초과. 


# dict
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
questions = list(map(int, input().split()))
dict_cards = {}

for card in cards:
    dict_cards[card] = True

for q in questions:
    if q in dict_cards:
        print('1', end=' ')
    else:
        print('0', end=' ')
