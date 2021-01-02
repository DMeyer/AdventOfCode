
def parseInput():
    # [(opcode, value), ...]
    instructions = []

    for line in open('2020/day8/input'):
        op, value = line.strip().split()
        instructions.append((op, int(value)))
    return instructions

def executeProgram(instructions):
    pc = 0
    accumulator = 0
    visited = set()

    while pc < len(instructions):
        if pc in visited:
            # If we reach here we have an infinite loop
            return accumulator, visited, pc

        visited.add(pc)

        opcode = instructions[pc][0]
        value = instructions[pc][1]

        if opcode == 'jmp':
            pc = pc + value
        elif opcode == 'acc':
            accumulator += value
            pc += 1
        elif opcode == 'nop':
            pc += 1

    # If we reach here its because we reached the end of the program
    return accumulator, visited, pc

def part1(instructions):
    accumulator, _, _ = executeProgram(instructions)
    return accumulator

def part2(instructions):

    # Find all of the visited instructins to identify the subset of instructions to be considered for a change
    # _, visited, _ = executeProgram(instructions)

    pc_of_last_instruction = len(instructions)

    # Execute the program with a flipped value
    for pc in range(len(instructions)): #visited:
        opcode = instructions[pc][0]

        if opcode == 'jmp' or opcode == 'nop':
            altered_instructions = list(instructions)

            if opcode == 'jmp':
                altered_instructions[pc] = ('nop', instructions[pc][1])
            elif opcode == 'nop':
                altered_instructions[pc] = ('jmp', instructions[pc][1])
            
            acc, _, fianl_pc = executeProgram(altered_instructions)
            
            if pc_of_last_instruction == fianl_pc:
                return acc
    
    return 'Failed'

instructions = parseInput()

print(f'Day6 Part1 Answer: {part1(instructions)}')
print(f'Day6 Part2 Answer: {part2(instructions)}')