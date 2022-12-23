import sys
sys.stdin = open('sample_input.txt')

delta = [(-1,0), (1,0), (0,-1), (0,1)]  # 상,하,좌,우

# 1. 현재 위치를 들고 다니지 않을 때
def work(x, y, road, skill):
    '''
    x, y : 좌표
    road : 지금까지 조성된 등산로의 길이
    skill : 공사유무
    '''
    global ans
    if road > ans : ans = road
    visited[x][y] = 1

    for d in delta:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # a. 현위치보다 낮은곳으로 이동할 때
            if land[x][y] > land[nx][ny]:
                work(nx, ny, road + 1, skill)
            # b. 현위치보다 높거나 같은 곳으로 이동할 때
            elif skill and land[x][y] > land[nx][ny] - K:
                tmp = land[nx][ny]  # 기록
                land[nx][ny] = land[nx][ny] - 1
                work(nx, ny, road + 1, 0)   # 공사를 했기 때문에(스킬 사용)
                land[nx][ny] = tmp

    visited[x][y] = 0

# 2. 현재 위치를 들고 다닐 때
def work2(x, y, h, road, skill):
    global ans
    if road > ans : ans = road
    visited[x][y] = 1

    for d in delta:
        nx = x + d[0]
        ny = y + d[1]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]: continue

        if h > land[nx][ny]:
            work2(nx, ny, land[nx][ny], road+1, skill)
        elif skill and h > land[nx][ny] - K:
            work2(nx, ny, land[x][y] - 1 , road+1, 0)
    visited[x][y] = 0



for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    land = [list(map(int,input().split())) for _ in range(N)]    # 등산로 부지
    visited = [[0]*N for n in range(N)]                          # 방문여부
    max_height = 0
    ans = 0

    for i in range(N):
        for j in range(N):
            if max_height < land[i][j]:
                max_height = land[i][j]

    for i in range(N):
        for j in range(N):
            if land[i][j] == max_height:
                # work(i, j, 1, 1)    # 좌표, 길, 스킬
                work2(i, j, max_height, 1, 1)
    print('#{} {}'.format(tc, ans))