class Solution:
    def __init__(self, input_file_path: str = "input"):
        with open(input_file_path, "r") as f:
            self.raw_data = f.read()
        self.lines = [line for line in self.raw_data.split("\n") if line]

    def part_one(self):
        pass

    def part_two(self):
        pass


if __name__ == "__main__":
    solution = Solution()
    print(f"Part one: {solution.part_one()}")
    print(f"Part two: {solution.part_two()}")