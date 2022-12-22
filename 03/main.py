from functools import reduce


def priority(a: chr) -> int:
    return a.isupper() * 26 + (ord(a.lower()) - ord('a') + 1)

# If the floor division returns 2, the game was won by the second player
if __name__ == '__main__':
    # open input file
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        total = 0
        badges_total = 0
        group = []
        for line in input_file:
            # exc. 1
            # split rucksack items into 2 halves
            first_part, second_part = line[:len(line)//2], line[len(line)//2:]
            # intersect two parts
            intersection = set(first_part).intersection(second_part).pop()
            # sum the priorities of intersections
            total += priority(intersection)
            # total += sum(priority(char) for char in intersection)

            # exc. 2
            # add Elf to the group
            group.append(line)
            # if the group is full
            if len(group) == 3:
                # get the badge
                # print(group[elf] for elf in group[1:])
                badge = reduce(lambda acc, x: set(acc).intersection(x.strip()), group).pop()
                # badge = set(group[0]).intersection(group.__class_getitem__)
                group.clear()
                badges_total += priority(badge)


        # Output
        print(f'Sum of repetitive items in both compartments is: {total}')
        print(f'Sum of group badges priority is: {badges_total}')