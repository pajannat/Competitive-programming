def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M, T = map(int, input().split())
    A = [-1] + list(map(int, input().split()))
    XY = []
    for _ in range(M):
        X, Y = map(int, input().split())
        XY.append([X, Y])
    
    # idxの範囲外参照対策
    XY.append([-1, -1])
    
    bonus_idx = 0

    # 処理
    # 部屋1からNまで順に進めていく
    # 部屋Nに到達する前に持ち時間がなくなったらexit
    for i in range(1, N):
        # 持ち時間を Ai 消費することで、部屋iから部屋i+1へ移動
        if T > A[i]:
            T -= A[i]
        # 移動できなかったらexit
        else:
            print('No')
            exit()
        
        # ボーナス部屋に到達したら持ち時間を増やす
        if i+1 == XY[bonus_idx][0]:
            T += XY[bonus_idx][1]
            bonus_idx += 1
    
    # 部屋Nに到達したらYesを出力
    print('Yes')


if __name__ == '__main__':
    main()