def Manhattan_dist(y1, x1, y2, x2):
    z1 = x1 + y1
    z2 = x2 + y2
    w1 = x1 - y1
    w2 = x2 - y2
    dist = max(abs(z1 - z2), abs(w1 - w2))
    return dist

def main():

    # 入力を受け取る
    R, C = map(int, input().split())
    maze = [] # 迷路の文字配列
    for i in range(R):
        maze.append(list(input().rstrip()))
    
    num_list = []
    for i in range(1, 10):
        num_list.append(str(i))
    
    num_zahyo = []

    # 処理
    for r in range(R):
        for c in range(C):
            if maze[r][c] in num_list:
                num_zahyo.append([maze[r][c], r, c])
    
    for r in range(R):
        for c in range(C):
            if maze[r][c] == '#':
                for zahyo in num_zahyo:
                    dist = Manhattan_dist(r, c, zahyo[1], zahyo[2])
                    if dist <= int(zahyo[0]):
                        maze[r][c] = '.'

    for r in range(R):
        for c in range(C):
            if maze[r][c] in num_list:
                maze[r][c] = '.'

    # 答えを出力
    for m in maze:
        print(''.join(m))


if __name__ == "__main__":
    main()