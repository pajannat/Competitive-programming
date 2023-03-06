from enum import Enum
from typing import List
import sys


class Pos:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


class Response(Enum):
    NOT_BROKEN = 0
    BROKEN = 1
    FINISH = 2
    INVALID = -1


class Field:

    def __init__(self, N: int, C: int):
        self.C = C
        self.is_broken = [[False] * N for _ in range(N)]
        self.total_cost = 0

    def query(self, y: int, x: int, power: int) -> Response:
        self.total_cost += power + self.C
        print(f"{y} {x} {power}", flush=True)
        res = Response(int(input()))
        if res in (Response.BROKEN, Response.FINISH):
            self.is_broken[y][x] = True
        return res


class Solver:

    def __init__(self, N: int, source_pos: List[Pos], house_pos: List[Pos], C: int):
        self.N = N
        self.source_pos = source_pos
        self.house_pos = house_pos
        self.C = C
        self.field = Field(N, C)

    def solve(self):
        # # from each house, go straight to the first source
        # for house in self.house_pos:
        #     self.move(house, self.source_pos[0])

        # それぞれの houceから, 最も近い水源へ進む
        for house in self.house_pos:
            source = min_Manhattan_dist_source(house, self.source_pos)
            self.move(house, source)        

        # should receive Response.FINISH and exit before entering here
        raise AssertionError()

    def move(self, start: Pos, goal: Pos):
        # you can output comment
        print(f"# move from ({start.y},{start.x}) to ({goal.y},{goal.x})")

        # down/up
        if start.y < goal.y:
            for y in range(start.y, goal.y, 1):
                self.destruct(y, start.x)
        else:
            for y in range(start.y, goal.y, -1):
                self.destruct(y, start.x)

        # right/left
        if start.x < goal.x:
            for x in range(start.x, goal.x + 1, 1):
                self.destruct(goal.y, x)
        else:
            for x in range(start.x, goal.x - 1, -1):
                self.destruct(goal.y, x)

    def destruct(self, y: int, x: int):
        # excavate (y, x) with fixed power until destruction
        power = 100
        while not self.field.is_broken[y][x]:
            result = self.field.query(y, x, power)
            if result == Response.FINISH:
                print(f"total_cost={self.field.total_cost}", file=sys.stderr)
                sys.exit(0)
            elif result == Response.INVALID:
                print(f"invalid: y={y} x={x}", file=sys.stderr)
                sys.exit(1)


def Manhattan_dist(y1, x1, y2, x2):
    z1 = x1 + y1
    z2 = x2 + y2
    w1 = x1 - y1
    w2 = x2 - y2
    dist = max(abs(z1 - z2), abs(w1 - w2))
    return dist

def min_Manhattan_dist_source(house_pos_i, source_pos):
    min_dist = 1000 # N=200 より, マンハッタン距離は400以下
    min_dist_source = source_pos[0]
    y1 = house_pos_i.y
    x1 = house_pos_i.x

    # house_pos_i から最短距離にある source を全探索で探す
    for source in source_pos:
        y2 = source.y
        x2 = source.x
        tmp_dist = Manhattan_dist(y1, x1, y2, x2)
        if tmp_dist < min_dist:
            min_dist = tmp_dist
            min_dist_source = source

    return min_dist_source


def main():
    N, W, K, C = [int(v) for v in input().split(" ")]
    source_pos = []
    house_pos = []

    for _ in range(W):
        y, x = (int(v) for v in input().split(" "))
        source_pos.append(Pos(y, x))
    for _ in range(K):
        y, x = (int(v) for v in input().split(" "))
        house_pos.append(Pos(y, x))

    solver = Solver(N, source_pos, house_pos, C)
    solver.solve()


if __name__ == "__main__":
    main()