


def row(boarding_pass):
    lower = 0
    upper = 127
    for c in boarding_pass[:-3]:
        if c == 'F':
            upper = int((lower + upper) / 2)
        else:
            lower = int((lower + upper + 1) / 2)
    return lower

def col(boarding_pass):
    lower = 0
    upper = 7
    for c in boarding_pass[-3:]:
        if c == 'L':
            upper = int((lower + upper) / 2)
        else:
            lower = int((lower + upper + 1) / 2)
    return lower

def seatId(boarding_pass):
    return (row(boarding_pass) * 8) + col(boarding_pass)

def buildOccupiedSeats():
    occupied_seats = set()
    for line in open("input"):
        boarding_pass = line.strip()
        occupied_seats.add(seatId(boarding_pass))
    return occupied_seats

def part1(occupied_seats):
    return max(occupied_seats)

def part2(occupied_seats):
    minimum = min(occupied_seats)
    maximum = max(occupied_seats)
    for i in range(minimum, maximum):
        if i not in occupied_seats:
            return i
    return -1


occupied_seats = buildOccupiedSeats()
print(f'Day 5 Part 1 Answer: {part1(occupied_seats)}')
print(f'Day 5 Part 2 Answer: {part2(occupied_seats)}')
