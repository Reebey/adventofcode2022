from functools import reduce
from itertools import permutations
import re

# returns bounding range, instead of [a,b)
def bounding_range(start: int, stop: int) -> range:
    return range(start, stop+1)

if __name__ == '__main__':
    # open input file
    with open('example.txt', 'r', encoding='utf-8') as input_file:
        fully_contains_count = 0
        contains_count = 0
        for line in input_file:
            # get the assigments list
            assignments = list(map(lambda x : list(bounding_range(*map(int,x.split('-')))), re.findall(r'\d+-\d+', line)))

            # check if one of pairs in assigments is fully overlapped
            if all(set(pair[0]).issubset(set(pair[1])) or set(pair[0]).issuperset(set(pair[1])) for pair in permutations(assignments, 2)):
                fully_contains_count += 1

            # check if intersection of any pair in assigments is not empty 
            if any(len(set(pair[0]).intersection(pair[1]))>0 for pair in permutations(assignments, 2)):
                contains_count += 1

        # Output
        print(f'Count of fully overlapped assigments is: {fully_contains_count}')
        print(f'Count of overlapped assigments is: {contains_count}')