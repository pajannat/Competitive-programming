def main():
    from sys import stdin
    input = stdin.readline
    
    S = input().rstrip()

    from collections import deque
    T = deque() 
    p = 0
    for s in S:
        if s == "R":
            p += 1
            p = p % 2
        elif p == 0:
            if T:
                if T[-1] == s:
                    T.pop()
                else:
                    T.append(s)
            else:
                T.append(s)
        elif p == 1:
            if T:
                if T[0] == s:
                    T.popleft()
                else:
                    T.appendleft(s)
            else:
                T.appendleft(s)

    if p == 1:
        T = reversed(T)
    T = "".join(T)

    print(T)
    
if __name__ == '__main__':
    main()