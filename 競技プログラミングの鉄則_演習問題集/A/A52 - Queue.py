def main():

    from collections import deque
    # 入力を受け取る
    Q = int(input())
    Query = []
    for _ in range(Q):
        tmp_input = list(input().split())
        tmp_query = []
        for idx, q in enumerate(tmp_input):
            if idx == 0:
                tmp_query.append(int(q))
            else:
                tmp_query.append(q)
        Query.append(tmp_query)
    
    ans = deque([])

    # 処理
    for q in Query:
        if q[0] == 1:
            ans.append(q[1])
        elif q[0] == 2:
            print(ans[0])
        elif q[0] == 3:
            ans.popleft()

 
if __name__ == "__main__":
    main()