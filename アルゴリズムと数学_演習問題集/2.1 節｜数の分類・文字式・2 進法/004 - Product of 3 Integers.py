def main():
    A = list(map(int, input().split()))

    ans = 1
    for a in A:
      ans *= a

    print(ans)
if __name__ == '__main__':
    main()