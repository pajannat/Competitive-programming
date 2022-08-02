def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    score = []

    for i in range(N):
        score.append([i, A[i], B[i], A[i]+B[i]])

    # 処理
    # score[i]を score[i][1], score[i][2], score[i][3] の3条件で降順ソート
    score.sort(key=lambda x:(x[1]), reverse=True)
    # sorted_data = sorted(score, key=lambda x:(x[1], x[2], x[3]), reverse=True)
    sorted_data = score[:X] + sorted(score[X:X+Y], key=lambda x:(x[2]), reverse=True)

    
    # 答えを出力
    for i in range(X+Y+Z):
        print(sorted_data[i][0])
    
    print(sorted_data)


if __name__ == '__main__':
    main()