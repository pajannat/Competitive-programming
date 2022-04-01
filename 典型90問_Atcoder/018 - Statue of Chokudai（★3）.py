def main():
    from sys import stdin
    input = stdin.readline

    import math
    # 入力を受け取る
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    
    for i in range(Q):
        E = int(input())
        sita = 2*math.pi*(-1/4-(E/T))
        y = (L/2)*(0 + math.cos(sita))
        z = (L/2)*(1 + math.sin(sita))

        if z == 0:
            ans = math.pi/2
        else:
            ans = math.atan( (((X-0)**2 + (Y-y)**2)**(0.5))/z )
        print(90 - ans*180/math.pi)  

if __name__ == '__main__':
    main()