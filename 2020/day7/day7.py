import re


def buildRules(file_path):
    rules = {}

    for line in open(file_path):
        # Get the name of the bag
        match_bag_name = re.search(r'^(\w+ \w+)', line)
        if match_bag_name:
            bag_name = match_bag_name.group()

            # Get the bags that bag_name can contain
            match_bags_contained = re.findall(r'(\d+) (\w+ \w+)', line)
            if match_bags_contained:
                rules[bag_name] = [(int(x), y)
                                   for x, y in match_bags_contained]
            else:
                rules[bag_name] = []
    return rules


def part1(rules):
    memo = {}  # key=bag, value=true|false

    # DFS traversal helper function
    def helper(bag):
        if bag == 'shiny gold':
            return True

        if bag in memo:
            return memo[bag]

        # for each bag that can be contained in bag
        found = False
        for _, contained_bag in rules[bag]:
            memo[contained_bag] = memo.get(
                contained_bag, False) | helper(contained_bag)
            found |= memo[contained_bag]

        memo[bag] = found
        return memo[bag]

    # Run a DFS traversal on each bag we have a rule for
    for bag in rules:
        helper(bag)

    # Count the number of bags that can at some point contain at least one shiny gold bag
    result = 0
    for bag in memo:
        if memo[bag]:
            result += 1

    # Subtracting 1 from the result since it contains the shiny gold bag as well
    return result - 1


def part2(rules):

    memo = {}

    def helper(bag):

        if bag in memo:
            return memo[bag]

        count = 1
        for quantity, contained_bag in rules[bag]:
            count += quantity * helper(contained_bag)

        memo[bag] = count
        return memo[bag]

    helper('shiny gold')

    # Subtracting 1 from the result since it contains the shiny gold bag as well
    return memo['shiny gold'] - 1


# rules = buildRules('2020/day7/test_part1')
# rules = buildRules('2020/day7/test_part2')
rules = buildRules('2020/day7/input')

print(f'Day6 Part1 Answer: {part1(rules)}')
print(f'Day6 Part2 Answer: {part2(rules)}')
