def main():
    from sys import stdin
    input = stdin.readline
    N = int(input())
    A = [int(i) for i in input().rstrip().split()]

    # AliceとBobの得点初期化
    AliceScore = 0
    BobScore = 0
    # カードを降順にソート
    A_sorted = sorted(A,reverse=True)
    # 大きいカードから順に取り出す
    for idx,num in enumerate(A_sorted):
        if idx%2 == 0:
            AliceScore += num
        else:
            BobScore += num
    
    print(AliceScore-BobScore)


if __name__ == '__main__':
    main()