from collections import deque

def parseInput(path):
    with open(path) as f:
        return [int(x.strip()) for x in f.readlines()]

def hasValidPreamble(numbers, index, preamble_size):
        preamble_set = set(numbers[index-preamble_size: index])

        for n in preamble_set:
            target = numbers[index] - n
            if target != n and target in preamble_set:
                return True
        return False

def part1(numbers):
    preamble_size = 25

    for i in range(preamble_size, len(numbers)):
        if not hasValidPreamble(numbers, i, preamble_size):
            return numbers[i]
    return 'Fail'

def part2(numbers):
    preamble_size = 25

    for i in range(preamble_size, len(numbers)):
        if not hasValidPreamble(numbers, i, preamble_size):
            invalid_index = i
            break

    # For all number previous to the invalid index we must sum a contigious window
    window_sum = 0
    windows_values = deque()
    for x in range(invalid_index):
        if window_sum == numbers[invalid_index]:
            return min(windows_values) + max(windows_values)

        new_number = numbers[x]
        windows_values.append(new_number)
        window_sum += new_number
        
        while window_sum > numbers[invalid_index]:
            # pop numbers in FIFO window until the sum of the window is less then our target allowing new numbers to be added
            pop_value = windows_values.popleft()
            window_sum -= pop_value

    return 'Fail'


numbers = parseInput('2020/day9/input')
print(f'Day9 Part1 Answer: {part1(numbers)}')
print(f'Day9 Part2 Answer: {part2(numbers)}')