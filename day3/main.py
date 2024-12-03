import re


# XD (estoy adicto a eval)
def mul(x: int, y: int) -> int:
    return x * y


class Solution:
    def __init__(self, input_file_path: str = "input"):
        with open(input_file_path, "r") as f:
            self.raw_data = f.read()
        self.lines = [line for line in self.raw_data.split("\n") if line]

    def part_one(self):
        pattern = r'(mul\(\d{1,3},\d{1,3}\))'
        instructions = [line for line in self.lines for line in re.findall(pattern, line)]
        return eval(" + ".join(instructions))

    def part_two(self):
        pattern = r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))'
        instructions = [line for line in self.lines for line in re.findall(pattern, line)]
        do = True
        result = []
        for instruction in instructions:
            if instruction.startswith("mul") and do:
                result.append(eval(instruction))
            elif instruction.startswith("don't()"):
                do = False
            elif instruction.startswith("do()"):
                do = True
        return sum(result)


if __name__ == "__main__":
    solution = Solution(input_file_path="input")
    example = Solution(input_file_path="example")
    print(f"Part one example: {example.part_one()}")
    print(f"Part one: {solution.part_one()}")
    print(f"Part two example: {example.part_two()}")
    print(f"Part two: {solution.part_two()}")
