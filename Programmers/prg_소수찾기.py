# 효율성이 안좋은코드
# def solution(n):
#     answer = 0
#     count = 0
#     for num in range(2,n+1):
#         for i in range(2,num):
#             if num % i == 0 :
#                 count = 1
#                 break
#         if count == 0:
#             answer += 1
#         count = 0
#     return answer

def solution(n):
    answer = 0
    list_sosu = []
    for 