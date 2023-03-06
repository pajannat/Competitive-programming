def main():

    # 入力を受け取る
    Q = int(input())
    A = []

    # 処理
    for _ in range(Q):
        query = list(input().split())
        if int(query[0]) == 1:
            A.append(query[1])
        elif int(query[0]) == 2:
            print(A[-1])
        elif int(query[0]) == 3:
            A.pop()        


if __name__ == "__main__":
    main()