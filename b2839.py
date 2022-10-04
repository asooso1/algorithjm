N = int(input())
toggle_cnt = 0
for i in range((N//3)+1):
    for j in range(N//5+1):
        if 5*j + 3*i == N:
            print(i+j)
            toggle_cnt = 1
            break
    if toggle_cnt:
        break
if not toggle_cnt:
    print(-1)