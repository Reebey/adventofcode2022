
# Return elves list, each elves is a list of a calories
def get_elves_from_file(file) -> list[list[int]]:
    elves = []
    elf = []
    for line in file.readlines():
        if line.isspace():
            elves.append(elf)
            elf = []
        else:
            elf.append(int(line.strip()))
    if len(elf) > 0:
        elves.append(elf)
    return elves

if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        elves = get_elves_from_file(input_file)
        
        # sort elves list descending based on their's sum
        elves.sort(reverse=True, key=sum)
        
        print(f'Most calories carried by single elf: {sum(elves[0])}')
        print(f'Most calories carried by three elves: {sum(map(sum,elves[0:3]))}')