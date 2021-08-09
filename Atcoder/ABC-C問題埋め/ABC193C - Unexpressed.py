def main():
    from sys import stdin
    input = stdin.readline
    # 10**10 < 2**35
    # 2 <= b <= 35 

    N = int(input())

    import math
    
    s = []
    A = math.ceil(math.sqrt(N))
    for a in range(2,A+1):
        for b in range(2,35):
            if N >= a**b:
                s.append(a**b)
            else:
                break
    s = set(s)
    
    print(N-len(s))

if __name__ == '__main__':
    main()