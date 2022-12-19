T = int(input())

ans = 0
# for i in range(T):
#     input_str = input()
#     str_list = []
#     for j in range(1,11):
#         str_list.append(input_str[0:j])     # 가능한 케이스 모두 list에 저장
    
#     for k in range(9,0,-1):                 # list value중 큰 단어부터 확인하기
#         if str_list[k] in input_str:
#             ans = k+1                       # index번호이기때문에 + 1
#             break
#     print(f'#{i+1} {ans}')

for i in range(T):
    input_str = input()
    for j in range(1,30):
        if input_str[0:j] == input_str[j:2*j]:
            ans = j
            break
    print(f'#{i+1} {ans}')