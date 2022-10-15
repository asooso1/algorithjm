prev_num, num = map(int,input().split(' '))
cnt = 0

while num != prev_num:
    if num % 10 == 1:
        num //= 10
        cnt += 1
    elif not num % 2 :
        num //= 2
        cnt += 1
    else :
        cnt = 0
        break
    if num < prev_num:
        cnt = 0
        break

if cnt:
    print(cnt+1)
else :
    print(-1)