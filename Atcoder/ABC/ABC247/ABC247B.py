def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    Names = []
    for _ in range(N):
        s, t = input().split()
        Names.append((s, t))

    # 処理
    flg = True
    for i in range(N):
        Name = Names[i]
        tmp_Names = Names[:i] + Names[i+1:]
        tmp_set = set()
        for tmp_Name in tmp_Names:
            tmp_set.add(tmp_Name[0])
            tmp_set.add(tmp_Name[1])

        if (Name[0] not in tmp_set) or (Name[1] not in tmp_set):
            pass
        else:
            flg = False
    
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()