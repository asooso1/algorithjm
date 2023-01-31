for tc in range(1, int(input())+1):
    N, M = input().split(' ')
    one_cnt = 0
    zero_cnt = 0
    for i in range(len(N)):
        if int(N[i]) ^ int(M[i]):
            if M[i] == '1':
                one_cnt += 1
            else:
                zero_cnt += 1
    
    if one_cnt >= zero_cnt:
        print(one_cnt)
    else :
        print(zero_cnt)
    
