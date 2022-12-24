import re

# returns string made of top crate of each stack on the platform
def crates_on_top(platform: list[list]) -> str:
    return ''.join([stack[-1] for stack in platform[1:]])


def move_crates(amount: int, start: int, stop: int, platform: list[list]) -> None:
    for crate in reversed(platform[start][-amount:]):
        platform[stop].append(crate) 
    platform[start] = platform[start][:-amount]

def move_crates_9001(amount: int, start: int, stop: int, platform: list[list]) -> None:
    for crate in platform[start][-amount:]:
        platform[stop].append(crate) 
    platform[start] = platform[start][:-amount]

# read crates data to the platform
# kinda spaghetti in C-style
def read_crates(header: str, footer_line: str) -> list[list]:
    platform = [[]]
    for v_index, number in enumerate(footer_line):
        # if its column index
        if number.isdigit():
            # make a new list to the 'platform'
            platform.append([])
            # add every letter from bottom to the top
            for h_index in reversed(range(len(header))):
                # skip whitespaces
                if not header[h_index][v_index].isspace():
                    platform[-1].append(header[h_index][v_index])
    return platform

if __name__ == '__main__':
    # open input file
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        # first read the header fully
        header = []
        for line in input_file:
            # whitespace line is a delimiter between header and body
            if (line.isspace()):
                break
            header.append(line)

        platform = read_crates(header, header.pop())
        platform_copy = [x[:] for x in platform]
        for line in input_file:
            move_input = list(map(int,re.findall(r'move (\d+) from (\d+) to (\d+)', line)[0]))
            # exc. 1
            move_crates(*move_input, platform)
            # exc. 2
            move_crates_9001(*move_input, platform_copy)
        
        # Output
        print(f'After rearrangament, on the top of each stacks ends: {crates_on_top(platform)}')
        print(f'After rearrangament with CrateMover 9001, on the top of each stacks ends: {crates_on_top(platform_copy)}')