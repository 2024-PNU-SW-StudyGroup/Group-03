n = int(input())
data = [[0] * n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n**2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
    available = []

    for i in range(n):
        for j in range(n):
            # 빈자리가 있다면
            if data[i][j] == 0:
                prefer, empty = 0, 0
                
                # 동서남북 방향 확인하여 
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                     
                    # 범위내에 있을 때
                    if 0 <= nx < n and 0 <= ny < n:
                        # 좋아하는 학생이 주위에 있다면 더해준다.
                        if data[nx][ny] in student[1:]:
                            prefer += 1
                            
                        # 빈자리가 있다면 더해준다.
                        if data[nx][ny] == 0:
                            empty += 1

                available.append((i, j, prefer, empty))
    # 정렬
    available.sort(key= lambda x: (-x[2], -x[3], x[0], x[1]))
    data[available[0][0]][available[0][1]] = student[0]

answer = 0
score = [0, 1, 10, 100, 1000]
students.sort()

for i in range(n):
    for j in range(n):
        count = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] in students[data[i][j] - 1]:
                    count += 1

        answer += score[count]

print(answer)