def main():
    from sys import stdin
    input = stdin.readline

    from collections import defaultdict

    # 入力を受け取る
    N = int(input())
    XY = []
    for i in range(N):
        X, Y = map(int, input().split())
        XY.append([X, Y])
    S = input().rstrip()

    Y_dict = defaultdict(lambda: defaultdict(list))
    Collision_flg = False
    for i in range(N):
        Y_dict[XY[i][1]]["L"] = [-1]
        Y_dict[XY[i][1]]["R"] = [10**9 + 10]

    for i in range(N):
        if S[i] == "L":
            Y_dict[XY[i][1]]["L"].append(XY[i][0])
        else:
            Y_dict[XY[i][1]]["R"].append(XY[i][0])


    for i in Y_dict:
        R_min = min(Y_dict[i]["R"])
        L_max = max(Y_dict[i]["L"])
        if R_min < L_max:
            Collision_flg = True


    if Collision_flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()