def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque
    # 入力を受け取る
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    # 左から順に埋めたとき、マス i を左端とするシールが何枚必要か
    num = [0 for _ in range(N)]
    # マス i におけるシールの厚み
    # マス i に何枚シールを貼るべきか判断するために使用
    seal_thickness = 0
    # i-L+2 ~ i マスについて、そのマスを始点とするシールが何枚あるか
    que = deque([])

    # 処理
    for i, a in enumerate(A):
        # 必要な厚みを満たすために, マス i に貼るシールの数
        num[i] = max(0, a-seal_thickness)
        # シールの厚みを更新
        seal_thickness += num[i]
        # que にnum[i]を格納
        que.append(num[i])
        # 次のマス i+1 から見て, 左端のqueが範囲外の場合はpop
        if len(que) >= L:
            pop_num = que.popleft()
            # popしたシール数を考慮してシールの厚みを更新
            seal_thickness -= pop_num
    
    # 答えを出力
    ans = 0
    for n in num:
        ans += n
    print(ans)


if __name__ == '__main__':
    main()