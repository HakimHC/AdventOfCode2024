import itertools


class Solution:
    def __init__(self, input_file_path: str = "input"):
        with open(input_file_path, "r") as f:
            self.raw_data = f.read()
        self.lines = [line for line in self.raw_data.split("\n") if line]
        self.equations = {}
        for line in self.lines:
            raw = line.split(": ")
            self.equations[int(raw[0])] = [int(x) for x in raw[1].split(" ")]

        self.operators = ["+", "*"]

    @staticmethod
    def evaluate_equation(numbers: list[int], operators: list[str]) -> int:
        result = numbers[0]
        for i in range(len(numbers) - 1):
            if operators[i] == "+":
                result = result + numbers[i + 1]
            elif operators[i] == "*":
                result = result * numbers[i + 1]
            elif operators[i] == "||":
                result = int(f"{result}{numbers[i + 1]}")
        return result

    @staticmethod
    def generate_operators(operators: list[str], numbers: list[int]) -> list[str]:
        return [x for x in itertools.product(operators, repeat=len(numbers) - 1)]

    def part_one(self):
        correct = []
        base_operators = ["+", "*"]
        for equation in self.equations:
            numbers = self.equations[equation]
            for operators in Solution.generate_operators(base_operators, numbers):
                result = self.evaluate_equation(numbers, operators)
                if result == equation:
                    correct.append(equation)
                    break

        return sum(correct)


    def part_two(self):
        correct = []
        base_operators = ["+", "*", "||"]
        for equation in self.equations:
            numbers = self.equations[equation]
            for operators in Solution.generate_operators(base_operators, numbers):
                result = self.evaluate_equation(numbers, operators)
                if result == equation:
                    correct.append(equation)
                    break
        return sum(correct)


if __name__ == "__main__":
    example = Solution(input_file_path="example")
    solution = Solution(input_file_path="input")
    print(f"Part one example: {example.part_one()}")
    print(f"Part one: {solution.part_one()}")
    print(f"Part two example: {example.part_two()}")
    print(f"Part two: {solution.part_two()}")
