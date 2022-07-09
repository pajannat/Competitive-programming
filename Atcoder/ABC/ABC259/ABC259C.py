def main():
    from sys import stdin
    input = stdin.readline

    from itertools import groupby

    def runLengthEncode(S: str) -> "List[tuple(str, int)]":
        grouped = groupby(S)
        res = []
        for k, v in grouped:
            res.append((k, int(len(list(v)))))
        return res


    # 入力を受け取る
    S = input().rstrip()
    T = input().rstrip()

    SS = runLengthEncode(S)
    TT = runLengthEncode(T)

    # 処理
    flg = True
    if len(SS) != len(TT):
        flg = False
    else:
        for i in range(len(SS)):
            if SS[i][0] != TT[i][0]:
                flg = False
            
            if SS[i][1] > TT[i][1]:
                flg = False
            elif SS[i][1] == TT[i][1]:
                pass
            elif SS[i][1] < TT[i][1]:
                if SS[i][1] == 1:
                    flg = False
    
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()