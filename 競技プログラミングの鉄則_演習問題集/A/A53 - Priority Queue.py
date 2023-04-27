def main():
    

    import heapq
    # 入力を受け取る
    Q = int(input())
    Query = []
    for _ in range(Q):
        Query.append(list(map(int, input().split())))
    
    ans = []
    heapq.heapify(ans)

    # 処理
    for q in Query:
        if q[0] == 1:
            heapq.heappush(ans, q[1])
        elif q[0] == 2:
            print(ans[0])
        elif q[0] == 3:
            heapq.heappop(ans)

 
if __name__ == "__main__":
    main()