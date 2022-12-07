import sys

sys.stdin = open('sample_input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],  # 상하좌우
    [0, 1, 0, 1],  # 상하
    [1, 0, 1, 0],  # 좌우
    [1, 0, 0, 1],  # 하우
    [1, 1, 0, 0],  # 하좌
    [0, 1, 1, 0],  # 하좌
    [0, 0, 1, 1],  # 상좌
]

for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    #지도 정보
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    Q = [(R, C)]
    visited[R][C] = 1

    ans = 0

    while Q:
        r, c = Q.pop(0)
        ans += 1

        if visited[r][c] >= L: continue
        # elif visited[r][c] > L: break

        # 사방향 탐색
        for d in range(4):
            curr_p = tunnel[r][c]
            # 현재 바라보는 방향으로 길이 없다면
            if pipe[curr_p][d] == 0: continue

            nr = r + dr[d]
            nc = c + dc[d]

            # 다음좌표가 맵을 벗어났다면
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue

            nd = (d + 2) % 4    #다음 방향
            np = tunnel[nr][nc] #다음 파이프

            # 방문을 했거나, 다음 좌표의 파이프가 현재좌표와 연결되지 않는다면
            if visited[nr][nc] or pipe[np][nd] == 0: continue

            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr,nc))
    print('#{} {}'.format(tc, ans))