string = input().split('-')
result = 0
answer = 0

for key, num_list in enumerate(string):
    result = 0
    if not key :
        for num in string[key].split('+'):
            result += int(num)
        answer += result
    else :
        for num in string[key].split('+'):
            result += int(num)
        answer -= result    
print(answer)