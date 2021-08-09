def main():
    from sys import stdin
    input = stdin.readline

    S = list(input().rstrip())

    list_S = [0]*len(S)
    for idx in range(len(S)):
        if S[idx] == '6':
            list_S[len(S)-1-idx] = '9'
        elif S[idx] == '9':
            list_S[len(S)-1-idx] = '6'
        else:
            list_S[len(S)-1-idx] = S[idx]

    print(''.join(list_S))
        
if __name__ == '__main__':
    main()