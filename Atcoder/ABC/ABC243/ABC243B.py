def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    set_A = set(A)
    set_B = set(B)

    cnt1 = 0
    for i in range(N):
        if A[i] == B[i]:
            cnt1 += 1
    
    cnt2 = len(set_A & set_B) - cnt1
    
    print(cnt1)
    print(cnt2)

if __name__ == '__main__':
    main()