# No.2047
input_str = input()
ans_str = ''
for char in input_str:
    if char.islower() == True :
        ans_str +=char.upper()
    else :
        ans_str += char
print(ans_str)