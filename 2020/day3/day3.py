# Advent Of Code Day 3

def buildForest():
    forest = []
    for line in open("input"):
        forest.append(list(line.strip()))
    return forest

def findTreeEncounters(forest, slope_x, slope_y):
    x = 0
    y = 0
    width = len(forest[0])
    height = len(forest)
    tree_encounters = 0

    def isTree(forest, x, y):
        return forest[y][x] == '#'

    while y < height:
        if isTree(forest, x % width, y % height):
            tree_encounters += 1
        x += slope_x
        y += slope_y
    return tree_encounters

def part1(forest):
    return findTreeEncounters(forest, 3, 1)

def part2(forest):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    result = 1 # This works since according to the problem we cannot have zero encounters
    for sx, sy in slopes:
        result *= findTreeEncounters(forest, sx, sy)
    return result

forest = buildForest()
print(f'Day3 Part1 Answer: {part1(forest)}')
print(f'Day3 Part2 Answer: {part2(forest)}')

