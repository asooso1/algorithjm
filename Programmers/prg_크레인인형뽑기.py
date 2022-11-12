def solution(board,moves):
    basket = []
    answer = 0
    for move in moves:
        for idx in range(len(board)):
            if not board[idx][move-1] :
                pass
            else :
                basket.append(board[idx][move-1])
                board[idx][move-1] = 0
                break


    i = 0
    basket.append(0)
    while i < len(basket)-1:
        if basket[i] == basket[i+1]:
            answer += 2
            basket.pop(i)
            basket.pop(i)
            i = 0
        else :
            i += 1
    basket.remove(0)
    return answer

# def solution(board,moves):
#     answer = 0
#     basket = []
#     for i in moves:
#         for j in range(len(board)):
#             if board[j][i-1] == 0:
#                 pass
#             else :
#                 basket.append(board[j][i-1])
#                 board[j][i-1] = 0
#                 break
#         if len(basket) >= 2 and (basket[len(basket)-1] == basket[len(basket)-2]) :
#             basket.pop(-1)
#             basket.pop(-1)
#             answer += 2
#     return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
print(solution([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,3],[3,3,3,3,3]],[1,5,3,5,1,2,1,4]))

# 4 3 1 1 3 2 4
# 3 3
