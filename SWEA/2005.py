T = int(input())

def pascal_triangle(num):
    for i in range(num):
        line_str = ''
        prev_line_list = []
        for j in range(num):
            line_str += str(i)+ ' '
            
for test_case in range(T):
    N = int(input())
    pascal_triangle(N)


# 재풀이
# T = int(input())
# for test_case in range(1,T+1):
#     N = int(input())
#     answer = []
#     for num in range(N):
#         answer.append([])

#     for i in range(N):
#         for j in range(i+1):
#             pass
#             if j == 0 or j == i:
#                 answer[i].append(1)
#             else :
#                 answer[i].append(answer[i-1][j]+answer[i-1][j-1])
            
    
#     print(f'#{test_case}')
#     for answer_line in answer:
#         print(*answer_line,sep=' ')