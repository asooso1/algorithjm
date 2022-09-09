import sys
sys.stdin = open('b1463.txt')

N = int(input())
cnt = 0
dp = [N]

while N != 1:
    if N % 3 == 0 or (N - 1) % 3 == 0:
        if N % 3 == 0:
            N /= 3
            cnt += 1
        else:
            N = (N - 1) / 3
            cnt += 2
    else:
        if N % 2 == 0:
            N /= 2
            cnt += 1
        else:
            N = (N - 1) / 2
            cnt += 2
    
    # if N % 3 == 0:
    #     cnt += 1
    #     N /= 3
    # elif N % 2 == 0:
    #     N /= 2
    # else:
    #     N -= 1
print(cnt)