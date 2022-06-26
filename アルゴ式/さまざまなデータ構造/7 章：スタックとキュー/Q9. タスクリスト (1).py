def main():
    from sys import stdin
    input = stdin.readline


    from collections import deque
    # 入力を受け取る
    Q = int(input())
    TODO_list = deque([])
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Set query
        if flg == 0:
            TODO_list.append(query[1])

        # Do query
        elif flg == 1:
            print(TODO_list.popleft())

if __name__ == '__main__':
    main()