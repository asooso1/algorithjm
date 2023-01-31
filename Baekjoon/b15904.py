input_str = input()
compare_list = ['U','C','P','C']
idx = 0
for char in input_str:
    if char.isupper():
        if char == compare_list[idx]:
            idx += 1
        else :
            continue
    if idx == 4:
        break
    
if idx == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')