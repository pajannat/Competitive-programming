def main():
    
    # 入力を受け取る
    A, B = map(int, input().split())

    # 処理
    
    # 答えを出力
    if A == (B//2):
        print("Yes")
    else:
        print("No")

 
if __name__ == "__main__":
    main()