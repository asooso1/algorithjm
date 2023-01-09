N = int(input())

ans_str = ''

for i in range(1,N+1):
    str_i = str(i)
    if ('3' in str_i) or ('6' in str_i) or ('9' in str_i) :
        for j in str_i:
            if (int(j) !=0) and (not int(j) % 3) :
                ans_str += '-'
            else :
                pass
    else :
        ans_str += str_i
    ans_str += ' '

print(ans_str)