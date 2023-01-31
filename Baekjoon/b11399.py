n = int(input())
list_person = list(map(int,input().split()))
list_person.sort()
delay = 0
answer = 0
for person in list_person:
    delay += person
    answer += delay
    
print(answer)