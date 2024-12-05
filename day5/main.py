import re


class Solution:
    def __init__(self, input_file_path: str = "input"):
        with open(input_file_path, "r") as f:
            self.raw_data = f.read()
        self.lines = [line for line in self.raw_data.split("\n") if line]
        self.rules = {}

        self.raw_rules = [line for line in self.lines if re.match(r'^\d{2}\|', line)]
        self.raw_updates = [line for line in self.lines if re.match(r'^\d{2},', line)]
        self.updates = [[int(x) for x in update.strip().split(",")] for update in self.raw_updates]

        for rule in self.raw_rules:
            key = int(rule.split("|")[0])
            value = int(rule.split("|")[1])
            if key not in self.rules:
                self.rules[key] = [value]
            else:
                self.rules[key].append(value)

    def is_number_in_order(self, i: int, update: list[int]):
        if i == 0:
            return True
        key = update[i]
        if key not in self.rules:
            return True
        while i > 0:
            i -= 1
            if update[i] in self.rules[key]:
                return False
        return True

    def part_one(self):
        good_updates = []
        for update in self.updates:
            correct_numbers = [self.is_number_in_order(i, update) for i in range(len(update))]
            if all(correct_numbers):
                good_updates.append(update)
        return sum([update[len(update) // 2] for update in good_updates])

    def part_two(self):
        bad_updates = []
        for update in self.updates:
            correct_numbers = [self.is_number_in_order(i, update) for i in range(len(update))]
            if not all(correct_numbers):
                bad_updates.append(update)

        for update in bad_updates:
            i = 0
            while i < len(update):
                if not self.is_number_in_order(i, update):
                    update[i], update[i - 1] = update[i - 1], update[i]
                    i -= 2
                i += 1
        return sum([update[len(update) // 2] for update in bad_updates])



if __name__ == "__main__":
    solution = Solution(input_file_path="input")
    example = Solution(input_file_path="example")
    print(f"Part one example: {example.part_one()}")
    print(f"Part one: {solution.part_one()}")
    print(f"Part two example: {example.part_two()}")
    print(f"Part two: {solution.part_two()}")
