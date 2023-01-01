# adds directory to pointer location
def add_dir(dir: str, pointer: dict) -> None:
    pointer.setdefault(dir, {'..': pointer})

# adds directory to pointer location
def add_file(file: str, size: int, pointer: dict) -> None:
    pointer.setdefault(file, size) 

# set pointer to the gived 'to' location
def cd(to: str, pointer: dict, root: dict) -> dict:
    match to:
        case '/':
            pointer = root
        case '..':
            pointer = pointer['..']
        case _:
            if to not in pointer:
                add_dir(to, pointer)
            pointer = pointer[to]
    return pointer

# return list of tuples (dir_name, storage_size)
def dir_dict(lst: list, pointer: dict) -> int:
    sum = 0
    for k, v in pointer.items():
        if k == '..':
            continue
        if type(v) is dict:
            dir_size = dir_dict(lst, pointer[k])
            lst.append((k, dir_size))
            sum += dir_size
        else:
            sum += v
    return sum

if __name__ == '__main__':
    # open input input
    root = {}
    pointer = None
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            words = line.split()
            if words[0] == '$':
                match words[1]:
                    case 'cd':
                        pointer = cd(words[2], pointer, root)
                    case _:
                        pass
            else:
                if words[0] == 'dir':
                    add_dir(words[1], pointer)
                else:
                    add_file(words[1], int(words[0]), pointer)


        dir_list = []
        dir_list.append(('/', dir_dict(dir_list, root)))
        # exc. 1
        at_most_100k_total_size = sum([v for k,v in dir_list if v <= 100_000])
        # exc. 2
        occupied_space = dir_list[-1][1] # last element is a root directory
        space_to_free = 30_000_000 - (70_000_000 - occupied_space)
        dir_list.sort(key=lambda x: x[1])
        to_delete = next((x for x in dir_list if x[1] >= space_to_free), None)

        # Output
        print(at_most_100k_total_size)
        print(f'Total size of directories which size is at most 100k: {at_most_100k_total_size}')
        print(f'Size of the directory to delete: {to_delete[1]}')