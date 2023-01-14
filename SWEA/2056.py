# No. 2056
T = int(input())
thirtyone=[1,3,5,7,8,10,12]
thirty=[4,6,9,11]

for i in range(0,T):
    date = input()
    year = int(date[0:4])
    mon = int(date[4:6])
    day = int(date[6:8])
    if 0 < mon < 13 :
        pass
        if mon in thirtyone:
            if 0 < day < 32:
                print(f'#{i+1} {date[0:4]}/{date[4:6]}/{date[6:8]}')
            else :
                print(f'#{i+1} -1')
        elif mon in thirty:
            if 0 < day < 31:
                print(f'#{i+1} {date[0:4]}/{date[4:6]}/{date[6:8]}')
            else :
                print(f'#{i+1} -1')
        elif mon == 2:
            if 0 < day < 29:
                print(f'#{i+1} {date[0:4]}/{date[4:6]}/{date[6:8]}')
            else :
                print(f'#{i+1} -1')
    else :
        print(f'#{i+1} -1')
    
