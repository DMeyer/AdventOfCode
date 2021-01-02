
def parseInput(path):
    with open(path) as f:
        return [int(x.strip()) for x in f.readlines()]


def part1(numbers):

    previous_adapter = 0
    current_adapter = 0
    dist = {}

    for x in range(len(numbers)):
        current_adapter = numbers[x]
        diff = current_adapter - previous_adapter
        dist[diff] = dist.get(diff, 0) + 1
        previous_adapter = current_adapter

    print(dist)
    return dist.get(1, 0) * dist.get(3, 0)


def part2(numbers):
    # Create the memo and initialize the first item
    memo = {}
    memo[0] = 1

    for adapter in numbers:
        memo[adapter] = memo.get(
            adapter - 1, 0) + memo.get(adapter - 2, 0) + memo.get(adapter - 3, 0)

    return memo[max(numbers)]


# numbers = parseInput('2020/day10/test_input')
numbers = parseInput('2020/day10/input')

# Sort the numbers so we start with the lowest valued adapter first
numbers = sorted(numbers)
# Add the internal adapter
numbers.append(numbers[-1] + 3)


print(f'Day9 Part1 Answer: {part1(list(numbers))}')
print(f'Day9 Part2 Answer: {part2(numbers)}')
