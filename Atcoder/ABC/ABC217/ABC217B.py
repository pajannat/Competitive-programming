def main():
    from sys import stdin
    input = stdin.readline

    S_list = []
    for _ in range(3):
        S_list.append(input().rstrip())
    contest_list = ["ABC", "ARC", "AGC", "AHC"]

    for s in S_list:
        contest_list.remove(s)

    print(contest_list[-1])

if __name__ == '__main__':
    main()