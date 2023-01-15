# No.2050
input_str = input()
int_list = []
for idx in input_str:  
    if ord(idx) < ord('a'):
        int_list.append(ord(idx)-64)
    elif ord(idx) >= ord('a'):
        int_list.append(ord(idx)-96)
    else :
        pass

ans_str = ''
for idx in int_list:
    ans_str += str(idx) +' '
print(ans_str[:-1:])