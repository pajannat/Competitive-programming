def main():
    from sys import stdin
    input = stdin.readline
    S = input().rstrip()
    S_changed = S[::-1]

    flg = False
    while True:
        if len(S_changed) == 0:
            print("YES")
            flg = True
            break
        elif len(S_changed) < 5:
            break

        elif S_changed[:7] == "dreamer"[::-1]:
            S_changed = S_changed[7:]
        elif S_changed[:5] == "dream"[::-1]:
            S_changed = S_changed[5:]
        elif S_changed[:6] == "eraser"[::-1]:
            S_changed = S_changed[6:]
        elif S_changed[:5] == "erase"[::-1]:
            S_changed = S_changed[5:]
        else:
            break
    
    if flg:
        pass
    else:
        print("NO")


if __name__ == '__main__':
    main()