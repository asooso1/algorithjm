num = int(input())
ans_str = '1 '
multi_total = 1
for i in range(1,num+1):
    multi_total *= 2
    ans_str += str(multi_total) + ' '
print(ans_str[:-1:])
