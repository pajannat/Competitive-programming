def main():
    from sys import stdin
    input = stdin.readline


    from collections import deque
    # 入力を受け取る
    X = int(input())
    Q = int(input())
    TODO_list = deque([])
    cnt = 0
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Push query
        if flg == 0:
            t = int(query[1])
            TODO_list.append(t)

        # Pop query
        elif flg == 1:
            t = int(query[1])

            # X経過したタスクがある限りタスクを消化済みとする
            # TODO_listが空の場合, "len(TODO_list) > 0"でwhileループ打ち切り
            # "t-X >= TODO_list[0]" は判定されないため, TODO_list[0]でのエラーは生じない
            while len(TODO_list) > 0 and (t-X >= TODO_list[0]):
                TODO_list.popleft()
                cnt += 1
                # TODO_list が空になったらbreak
                if len(TODO_list) == 0:
                    break

            # 消化済みタスクの数を出力
            print(cnt)


if __name__ == '__main__':
    main()