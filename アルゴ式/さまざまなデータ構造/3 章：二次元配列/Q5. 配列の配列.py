def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, T = input().split()
    N = int(N)
    student_colors_list = [list(input().split()) for _ in range(N)]
    
    # 処理
    cnt = 0
    for student_colors in student_colors_list:
        if T in student_colors:
            cnt += 1
    
    # 答えを出力
    print(cnt)

if __name__ == '__main__':
    main()