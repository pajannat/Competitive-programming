def main():
    from sys import stdin
    input = stdin.readline

    import numpy

    def cross_product(ax, ay, bx, by, cx, cy):
        vec_AB = [bx-ax, by-ay]
        vec_AC = [cx-ax, cy-ay]

        return numpy.cross(vec_AB, vec_AC)

    # 三角形ABCにDが含まれるか判断
    def solver(A, B, C, D):
        flg_include = False
        cross_ABxAD = cross_product(A[0], A[1], B[0], B[1], D[0], D[1])
        cross_BCxBD = cross_product(B[0], B[1], C[0], C[1], D[0], D[1])
        cross_CAxCD = cross_product(C[0], C[1], A[0], A[1], D[0], D[1])
        if cross_ABxAD > 0 and cross_BCxBD > 0 and cross_CAxCD > 0:
            pass
        else:
            flg_include = True
        return flg_include

    # 入力を受け取る
    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())
    Cx, Cy = map(int, input().split())
    Dx, Dy = map(int, input().split())

    # どの3点を三角形の頂点とし、どの1点の内包を判定するかを示すリスト
    Input_list = [
        [[Ax, Ay], [Bx, By], [Cx, Cy], [Dx, Dy]],
        [[Dx, Dy], [Ax, Ay], [Bx, By], [Cx, Cy]],
        [[Cx, Cy], [Dx, Dy], [Ax, Ay], [Bx, By]],
        [[Bx, By], [Cx, Cy], [Dx, Dy], [Ax, Ay]]
        ]

    # 処理
    for lis in Input_list:
        # 選んだ1点が他三点からなる三角形に内包されるかを判定
        flg = solver(*lis)

        # flg == False となることがあれば, "No"を出力して終了
        if flg == False:
            print("No")
            exit()
    
    # flg == False となることがなければ, "Yes"を出力
    print("Yes")


if __name__ == '__main__':
    main()