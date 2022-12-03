N = int(input())
ans_str = ''
for i in range(1,N+1):
    if N % i == 0:
        ans_str += str(i) + ' ' 
    else :
        pass
print(ans_str[:-1:])