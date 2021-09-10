def main():
    from sys import stdin
    input = stdin.readline

    import bisect
    import array

    L, Q = map(int, input().split())

    B = array.array("i", [0, L])
    
    for i in range(Q):
        c, x = map(int, input().split())

        if c == 1:
            B.insert(bisect.bisect_left(B, x), x)
        else:
            left_i = bisect.bisect_left(B, x) - 1
            right_i = bisect.bisect_right(B, x)
            print(B[right_i] - B[left_i])
            

if __name__ == '__main__':
    main()