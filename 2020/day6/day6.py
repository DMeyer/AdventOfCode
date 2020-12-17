# Advent Of Code Day 6
# Note: I added a blank line at the end of the input file to simplify parsing

def part1():
    count = 0
    unique_questions = set()
    
    for line in open("input"):
        questions = line.strip()
        if len(questions):
            unique_questions.update(questions)
        else:
            count += len(unique_questions)
            unique_questions = set()
    return count


def part2():
    answer_counts = {}
    people_in_group = 0
    result = 0

    def questions_all_answered_yes(answer_counts, people):
        count = 0
        for v in answer_counts.values():
            if v == people:
                count += 1
        return count

    for line in open("input"):
        questions = line.strip()
        if len(questions):
            people_in_group += 1
            for q in questions:
                answer_counts[q] = answer_counts.get(q, 0) + 1
        else:
            result += questions_all_answered_yes(answer_counts, people_in_group)
            answer_counts = {}
            people_in_group = 0
    return result

print(f'Day6 Part1 Answer: {part1()}')
print(f'Day6 Part2 Answer: {part2()}')
