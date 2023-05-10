import sys
sys.stdin = open('b25192.txt')


N=int(input())

dict_message={}

cnt=0

for _ in range(N):
    message=input()

    if message=="ENTER":
        for key,value in dict_message.items():
            if value==1:
                cnt+=1
        dict_message={}
    else:
        if message not in dict_message:
            dict_message[message]=1

for key,value in dict_message.items():
    if value==1:
        cnt+=1

print(cnt)