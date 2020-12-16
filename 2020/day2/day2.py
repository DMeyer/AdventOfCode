# Advent of Code Day 2 

class Password:
    def __init__(self, letter_min, letter_max, letter, password):
        self.letter_min = letter_min
        self.letter_max = letter_max
        self.letter = letter
        self.password = password

def inputLineParser(line):
    min_max, letter, password = line.strip().split(' ')
    letter_min, letter_max = min_max.split('-')
    return Password(
        int(letter_min),
        int(letter_max),
        letter[0],
        password
    )

def part1(passwords):
    def isPasswordValid(p):
        ''' 
        The password is valid if [p.letter_min <= count(p.letter) <= p.letter_max]
        '''
        count = 0
        for l in p.password:
            if l == p.letter:
                count += 1
            if count > p.letter_max:
                return False
        return (count >= p.letter_min) and (count <= p.letter_max)

    valid_passwords = 0
    for p in passwords:
        if isPasswordValid(p):
            valid_passwords += 1
    return valid_passwords

def part2(passwords):
    def isPasswordValid(p):
        '''
        The password is valid if letter is in one of p.letter_min or p.letter_max but not both
        '''
        a = (p.password[p.letter_min - 1] == p.letter)
        b = (p.password[p.letter_max - 1] == p.letter)
        return a ^ b

    valid_passwords = 0
    for p in passwords:
        if isPasswordValid(p):
            valid_passwords += 1
    return valid_passwords

# Build passwords
passwords = []
for line in open("input"):
    passwords.append(inputLineParser(line))

# Day 2 part 1
print(f'Day2 Part1 Answer: {part1(passwords)}')
print(f'Day2 Part2 Answer: {part2(passwords)}')
