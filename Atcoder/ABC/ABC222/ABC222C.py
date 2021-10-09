def main():
    from sys import stdin
    input = stdin.readline

    N, M = map(int, input().split())
    A = [list(input().rstrip()) for _ in range(2*N)]
    win_cnt = [[0, (i+1)] for i in range(2*N)]
    # print(win_cnt)

    for i in range(M):
        for j in range(0, N):
            player1_num = win_cnt[2*j][1] - 1
            player2_num = win_cnt[2*j+1][1] - 1

            # じゃんけんの手を格納
            player1_GCP = A[player1_num][i]
            player2_GCP = A[player2_num][i]

            # じゃんけんの勝ち負け判定
            if player1_GCP == player2_GCP:
                pass
            else:
                if player1_GCP == "G":
                    if player2_GCP == "C":
                        win_cnt[2*j][0] += 1
                    elif player2_GCP == "P":
                        win_cnt[2*j+1][0] += 1
                elif player1_GCP == "C":
                    if player2_GCP == "G":
                        win_cnt[2*j+1][0] += 1
                    elif player2_GCP == "P":
                        win_cnt[2*j][0] += 1
                elif player1_GCP == "P":
                    if player2_GCP == "G":
                        win_cnt[2*j][0] += 1
                    elif player2_GCP == "C":
                        win_cnt[2*j+1][0] += 1
        
        win_cnt.sort(key=lambda x: x[1])
        win_cnt.sort(reverse=True, key=lambda x: x[0])

    for i in range(N):
        print(win_cnt[2*i][1])
        print(win_cnt[2*i+1][1])

if __name__ == '__main__':
    main()