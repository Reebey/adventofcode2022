from itertools import takewhile

# counts number of seeable trees in 'given direction'
def length(tw: list, sl: list) -> int:
    if len(tw) == len(sl):
        return len(sl)
    return len(tw)+1

# returns number of trees able to see from given position
def seeable_trees_count(dx: int, dy: int, grid: list[list]) -> int:
    # make 2 lines, horizontal and vertical
    horizontal, vertical = grid[dy], [grid[y][dx] for y in range(len(grid))]
    tree = grid[dy][dx]

    score = 1
    sublists = [list(reversed(horizontal[:dx])),horizontal[dx+1:],list(reversed(vertical[:dy])),vertical[dy+1:]]
    m = []
    for sublist in sublists:
        trees_seq = list(takewhile(lambda t: t < tree,sublist))
        m.append(trees_seq)
        score *= length(trees_seq,sublist)
    return score

# checks if a tree is visible from outside the grid
def is_visible(dx: int, dy: int, grid: list[list]) -> bool:
    if dy in [0, len(grid)-1] or dx in [0, len(grid[dy])-1]:
        return True
    # make 2 lines, horizontal and vertical
    horizontal, vertical = grid[dy], [grid[y][dx] for y in range(len(grid))]
    tree = grid[dy][dx]
    # if all of any left/right/up/down tree is bigger
    return not (any(t >= tree for t in horizontal[:dx]) and \
           any(t >= tree for t in horizontal[dx+1:]) and \
           any(t >= tree for t in vertical[dy+1:]) and \
           any(t >= tree for t in vertical[:dy]))

if __name__ == '__main__':
    # open input input
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        grid = []
        for line in input_file:
            grid.append([int(c) for c in line if c.isdigit()])
        sum = 0
        max = 0
        for dy in range(len(grid)):
            for dx in range(len(grid[dy])):
                # exc. 1
                sum += is_visible(dx,dy,grid)
                # exc. 2
                if max < seeable_trees_count(dx,dy,grid):
                    max = seeable_trees_count(dx,dy,grid)

        # Output
        print(f'Number of visible trees outside the grid is: {sum}')
        print(f'Highest possible scenic score for any tree is: {max}')