T = int(input())

for test_case in range(1,T+1):
    P, Q, R, S, W = map(int, input().split())
    A_fee = P * W
    if W < R :
        B_fee = Q
    else :
        B_fee = Q + (W - R) * S
    if A_fee > B_fee :
        print(f'#{test_case} {B_fee}') 
    else :
        print(f'#{test_case} {A_fee}')