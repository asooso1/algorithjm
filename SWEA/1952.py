import sys
sys.stdin = open('sample_input.txt')

def calc(cost, m):  # m : 현재 월
    global min_cost
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return
    # # 1일권
    # calc(cost + (d * monthly_plan[m]), m+1)
    # # 한달권
    # calc(cost + m1, m+1)
    # 1일권 or 한달권
    calc(cost + min(d * monthly_plan[m], m1), m+1)
    # 3달권
    calc(cost + m3, m+3)

for tc in range(1, int(input())+1):
    d, m1, m3, y = map(int, input().split())    #1일권, 한달권, 세달권, 연간권

    monthly_plan = [0] + list(map(int, input().split()))    # 각 월별 계획

    min_cost = y # 1년치 비용이 현재 최저가라고 생각
    calc(0, 1)
    print('#{} {}'.format(tc, min_cost))