def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S1 = input().rstrip()
    S2 = input().rstrip()

    flg = True
    if (S1 == "#.") and (S2 == ".#"):
        flg = False
    
    if (S1 == ".#") and (S2 == "#."):
        flg = False 
    
    # 出力
    if flg:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()