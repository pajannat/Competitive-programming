def main():
    from sys import stdin
    import numpy as np
    input = stdin.readline

    N = int(input())
    A = [int(i) for i in input().split()]
    A = np.array(A)
    
    cnt = 0
    while True:
        if np.all(A%2 == 0):
            A = A/2
            cnt += 1
        else:
            break
    print(cnt)

if __name__ == '__main__':
    main()
