# checks if the given cycle should be registered
def should_be_registered(cycle: int) -> bool:
    return (cycle + 20) % 40 == 0

def draw_on_crt(cycle: int, x: int, crt_output: list) -> None:
    h_index = cycle % 40
    if h_index == 0:
        crt_output.append('\n')
    if abs(x - h_index) <= 1:
        crt_output.append('#')
    else:
        crt_output.append('.')

# increments the cycle, and registers
def next_cycle(cycle: int, X: int, register: list) -> None:
    cycle += 1
    if should_be_registered(cycle):
        register.append((cycle, X))
    
    return cycle

if __name__ == '__main__':
    # open input input
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        X: int = 1
        cycle: int = 1
        register: list = []
        crt_output: list = ['.']
        for line in input_file:
            words = line.split()
            if len(words) > 1:
                # addx
                draw_on_crt(cycle, X, crt_output)
                cycle = next_cycle(cycle, X, register)
                X += int(words[1])
                draw_on_crt(cycle, X, crt_output)
                cycle = next_cycle(cycle, X, register)
            else:
                # noop
                draw_on_crt(cycle, X, crt_output)
                cycle = next_cycle(cycle, X, register)

        # Output
        print(f'Sum of the six signals: {sum(cycle * x for cycle, x in register)}')
        print(f'Eight capital letters appeared on the screen:\n{"".join(crt_output)}')