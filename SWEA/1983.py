T = int(input())
for test_case in range(1,T+1):
    N, k = map(int,input().split(' '))
    students = list()
    grade = ['A', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    for i in range(N):
        middle, final, workshop = map(int,input().split())
        total = middle * 0.35 + final * 0.45 + workshop * 0.2
        students.append(round(total,2))
    print
    up_student = 0
    for student in students:
        if student > students[k-1]:
            up_student += 1
    answer = grade[up_student // (N//10)]
    print(f'#{test_case} {answer}')