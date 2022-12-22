from enum import Enum

class Sign(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

class Taunt(Enum):
    A = Sign.Rock
    B = Sign.Paper
    C = Sign.Scissors

class Response(Enum):
    X = Sign.Rock
    Y = Sign.Paper
    Z = Sign.Scissors

# Returns round result
# 6 - win, 3 - draw, 0 - lose
def round_result(a: Taunt, b: Response) -> int:
    return ((b.value.value-a.value.value+1)%3)*3

# 6 - win, 3 - draw, 0 - lose
# X - lose, Y - draw, Z - win
# X: A -> Z, B -> X, C -> Y -1 :1
# Y: A -> X, B -> Y, C -> Z  0 :2
# Z: A -> Y, B -> Z, C -> X +1 :3
def expected_response(a: Taunt, b: Response) -> Sign:
    return Sign((a.value.value+b.value.value)%3+1)

# If the floor division returns 2, the game was won by the second player
if __name__ == '__main__':
    # open input file
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        total_score, total_score_with_hint = 0, 0
        for line in input_file:
            # get input values
            words = line.split()
            taunt, response = Taunt[words[0]], Response[words[1]]
            # exc. 1
            total_score += round_result(taunt, response) + response.value.value
            # exc. 2
            expect_response = Response(expected_response(taunt, response)) 
            total_score_with_hint += round_result(taunt, expect_response) + expect_response.value.value 
        
        # Output
        print(f'If everything goes to the strategy guide, the total score would be: {total_score}')
        print(f'Taking into account Elf hint, the total score would be: {total_score_with_hint}')