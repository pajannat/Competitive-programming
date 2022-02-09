def main():
    N, X, Y = map(int, input().split())

    cnt = 0
    for i in range(1, N+1):
      if (i%X==0) or (i%Y==0):
        cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()