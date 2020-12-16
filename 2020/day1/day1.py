# Advent Of Code Day 1

def inputLineParser(line):
    return int(line.strip())

def part1(numbers):

    number_set = set(numbers)

    for num in numbers:
        target = 2020 - num

        if target in number_set:
            return target * num
    return -1

def part2(numbers):
    number_set = set(numbers)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            target = 2020 - numbers[i] - numbers[j]

            if target in number_set:
                return numbers[i] * numbers[j] * target
    return -1

numbers = []
for line in open('input'):
    numbers.append(inputLineParser(line))

print(f'Day1 Part1 Answer: {part1(numbers)}')
print(f'Day1 Part2 Answer: {part2(numbers)}')
