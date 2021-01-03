
def parseInput(path):
    with open(path) as f:
        lines = [l.strip() for l in f.readlines()]
        return list(map(lambda x: (x[0], int(x[1:])), lines))


class Ship:
    def __init__(self):
        self.position = [0, 0]  # N/S, E/W
        self.direction = 0
        self.waypoint_position = [1, 10]

    def updatePositionPart1(self, command):
        if command[0] == 'N':
            self.position[0] += command[1]
        elif command[0] == 'S':
            self.position[0] -= command[1]
        elif command[0] == 'E':
            self.position[1] += command[1]
        elif command[0] == 'W':
            self.position[1] -= command[1]
        elif command[0] == 'L':
            self.direction = (self.direction - command[1]) % 360
        elif command[0] == 'R':
            self.direction = (self.direction + command[1]) % 360
        elif command[0] == 'F':
            if self.direction == 0:  # east
                self.position[1] += command[1]
            elif self.direction == 90:  # south
                self.position[0] -= command[1]
            elif self.direction == 180:  # west
                self.position[1] -= command[1]
            elif self.direction == 270:  # north
                self.position[0] += command[1]


    def updatePositionPart2(self, command):
        if command[0] == 'N':
            self.waypoint_position[0] += command[1]
        elif command[0] == 'S':
            self.waypoint_position[0] -= command[1]
        elif command[0] == 'E':
            self.waypoint_position[1] += command[1]
        elif command[0] == 'W':
            self.waypoint_position[1] -= command[1]
        elif command[0] == 'L': # rotate counter clockwise
            rotation = (0 - command[1]) % 360
            while rotation > 0:
                self.rotateClockwise90()
                rotation -= 90
        elif command[0] == 'R':  # rotate clockwise
            rotation = command[1]
            while rotation > 0:
                self.rotateClockwise90()
                rotation -= 90
        elif command[0] == 'F':
            self.position[0] += (self.waypoint_position[0] * command[1])
            self.position[1] += (self.waypoint_position[1] * command[1])
            

    def rotateClockwise90(self):
        a = self.waypoint_position[0]
        b = self.waypoint_position[1]

        if a >= 0 and b >= 0:
            new = [-b, a]
        elif a < 0 and b >= 0:
            new = [-b, a]
        elif a < 0 and b < 0:
            new = [-b, a]
        elif a >= 0 and b < 0:
            new = [-b, a]

        self.waypoint_position = new

    def manhattan_distance(self):
        return abs(self.position[0]) + abs(self.position[1])


def part1(instructions):
    ship = Ship()
    for i in instructions:
        ship.updatePositionPart1(i)
    return ship.manhattan_distance()


def part2(instructions):
    ship = Ship()
    for i in instructions:
        ship.updatePositionPart2(i)
    return ship.manhattan_distance()


instructions = parseInput('2020/day12/input')
print(f'Day12 Part1 Answer: {part1(instructions)}')
print(f'Day12 Part2 Answer: {part2(instructions)}')
