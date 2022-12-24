# returns end of every distinct character substring of given length
def get_marker_index(start: int, length: int, string: str):
    set_length = len(set(string[start:start+length]))
    if set_length == length:
        print(set(string[start:start+length]), start, length)
        return start + set_length
    return 0

if __name__ == '__main__':
    # open input input
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        sop_index = 0
        sop_marker_length = 4
        som_index = 0
        som_marker_length = 14
        for line in input_file:
            for i in range(len(line) - sop_marker_length):
                if sop_index == 0: # exc. 1
                    sop_index = get_marker_index(i, sop_marker_length, line)
                elif som_index == 0: # exc. 2
                    som_index = get_marker_index(i, som_marker_length, line)
                else:
                    break
            break

        # Output
        print(f'Number of characters processed before detect first start-of-packet: {sop_index}')
        print(f'Number of characters processed before detect first start-of-message: {som_index}')