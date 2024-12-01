class Solution:
    def __init__(self, input_file_path: str = "input"):
        with open(input_file_path, "r") as f:
            self.raw_data = f.read()
        self.lines = [line for line in self.raw_data.split("\n") if line]
        self.list_a = [int(line.split()[0]) for line in self.lines if line]
        self.list_b = [int(line.split()[1]) for line in self.lines if line]

    def part_one(self):
        sorted_a = sorted(self.list_a)
        sorted_b = sorted(self.list_b)

        distances = [abs(a - b) for a, b in zip(sorted_a, sorted_b)]
        return sum(distances)

    def part_two(self):
        similarity_score = [x * self.list_b.count(x) for x in self.list_a]
        return sum(similarity_score)


if __name__ == "__main__":
    solution = Solution(input_file_path="input")
    example = Solution("example")
    print(f"Part one example: {example.part_one()}")
    print(f"Part one: {solution.part_one()}")
    print(f"Part two example: {example.part_two()}")
    print(f"Part two: {solution.part_two()}")
