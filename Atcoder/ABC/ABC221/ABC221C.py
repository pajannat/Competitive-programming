def main():
    from sys import stdin
    input = stdin.readline

    import itertools

    N = str(input().rstrip())

    ans = 0
    
    #長さを指定
    n = len(N)
    for bit_list in itertools.product([0, 1], repeat=n):
        A = []
        B = []
        for i, bit in enumerate(bit_list):
            if bit == 1:
                A.append(N[i])
            else:
                B.append(N[i])

        if len(A) == 0 or len(B) == 0:
            continue

        A.sort(reverse=True)
        B.sort(reverse=True)

        a = ""
        for s in A:
            a += s
        a = int(a)

        b = ""
        for s in B:
            b += s
        b = int(b)

        ans = max(ans, a*b)

    print(ans)   

if __name__ == '__main__':
    main()