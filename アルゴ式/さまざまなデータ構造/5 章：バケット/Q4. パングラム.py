def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    w = list(input().split())
    counter = [0 for _ in range(26)]

    # 処理
    for word in w:
        for s in word:
            # a-z -> 97-122 を a-z -> 0-25に変換する
            num = ord(s) - ord("a")
            counter[num] += 1
    
    # 1回もcountされていない文字があればFalse
    flg = True
    for x in counter:
        if x == 0:
            flg = False

    # cnt_dict = {}
    # a_to_z = "abcdefghijklmnopqrstuvwxyz"
    # for s in a_to_z:
    #     cnt_dict[s] = 0

    # # 処理
    # for word in w:
    #     for s in word:
    #         cnt_dict[s] += 1
    
    # flg = True
    # for s in a_to_z:
    #     if cnt_dict[s] == 0:
    #         flg = False
    
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()