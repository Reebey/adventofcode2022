from enum import Enum

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shiftTo(self, __o: object) -> object:
        self.x = __o.x
        self.y = __o.y
        return self

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __add__(self, __o: object) -> object:
        return Point(self.x+__o.x, self.y+__o.y)

    def __sub__(self, __o: object) -> object:
        return Point(self.x-__o.x, self.y-__o.y)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return self.__str__()

    def __copy__(self) -> object:
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

class Direction(Enum):
    U = Point(0,1)
    D = Point(0,-1)
    L = Point(-1,0)
    R = Point(1,0)

# bring number closer to 0 by 1
def bring_closer_to_zero(number: int) -> int:
    if number > 0:
        return number - 1
    elif number < 0:
        return number + 1
    return number

# calculates new tail position
def new_tail(head: Point, tail: Point) -> Point:
    diff_point = head - tail
    is_tail_close = True

    if abs(diff_point.x) > 1:
        diff_point.x = bring_closer_to_zero(diff_point.x)
        is_tail_close = False
    if abs(diff_point.y) > 1:
        diff_point.y = bring_closer_to_zero(diff_point.y)
        is_tail_close = False

    if is_tail_close:
        return tail
    else:
        return tail + diff_point

# moves knots in the given direction
def move(direction: Direction, steps: int, knots: list[Point], visits: set) -> None:
    for _ in range(steps):
        # first move the head knot
        knots[0].shiftTo(knots[0] + direction.value)
        # then fix rest of the knots
        for head, tail in zip(knots[0:-1], knots[1:]):
            tail.shiftTo(new_tail(head, tail))
        # add new knots position to a set
        visits.add(knots[-1].__copy__())

if __name__ == '__main__':
    # open input input
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        two_knots_rope = [Point(0,0) for _ in range(2)]
        first_rope_tail_visits = set([Point(0,0)])
        ten_knots_rope = [Point(0,0) for _ in range(10)]
        second_rope_tail_visits = set([Point(0,0)])
        for line in input_file:
            words = line.split()
            move(Direction[words[0]], int(words[1]), two_knots_rope, first_rope_tail_visits)
            move(Direction[words[0]], int(words[1]), ten_knots_rope, second_rope_tail_visits)

        # Output
        print(f'Number of 2 knots rope tail visit at least once is: {len(first_rope_tail_visits)}')
        print(f'Number of 10 knots rope tail visit at least once is: {len(second_rope_tail_visits)}')