num = int(input())
ans_str = ''
for i in range(num+1):
    ans_str = ' ' + str(i) + ans_str
print(ans_str[1:])