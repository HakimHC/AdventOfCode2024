import enum
from itertools import chain


class Direction(enum.Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UPLEFT = (-1, -1)
    UPRIGHT = (1, -1)
    DOWNLEFT = (-1, 1)
    DOWNRIGHT = (1, 1)


class Solution:
    def __init__(self, input_file_path: str = "input"):
        with open(input_file_path, "r") as f:
            self.raw_data = f.read()
        self.lines = [line for line in self.raw_data.split("\n") if line]
        self.max_x = len(self.lines[0])
        self.max_y = len(self.lines)

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.max_x and 0 <= y < self.max_y

    def get_word_in_direction(self, x: int, y: int, direction: Direction, word: str) -> str:
        counter = 0
        result = ""
        while self.in_bounds(x, y) and counter < len(word):
            result += self.lines[y][x]
            x += direction.value[0]
            y += direction.value[1]
            counter += 1
        return result

    def get_mas(self, x: int, y: int) -> bool:
        first = self.get_word_in_direction(x, y, Direction.DOWNRIGHT, "MAS")
        second = self.get_word_in_direction(x + 2, y, Direction.DOWNLEFT, "MAS")
        if first in ("MAS", "SAM") and second in ("MAS", "SAM"):
            return True
        return False

    def part_one(self):
        directions = [
            Direction.UPRIGHT,
            Direction.RIGHT,
            Direction.DOWNRIGHT,
            Direction.DOWN,
        ]
        result = 0
        for y in range(len(self.lines)):
            for x in range(len(self.lines[y])):
                for direction in directions:
                    word = self.get_word_in_direction(
                        x=x,
                        y=y,
                        direction=direction,
                        word="XMAS"
                    )
                    if word in ("XMAS", "SAMX"):
                        result += 1
        return result

    def part_two(self):
        result = 0
        for y in range(len(self.lines)):
            for x in range(len(self.lines[y])):
                if self.get_mas(x, y):
                    result += 1
        return result


if __name__ == "__main__":
    solution = Solution(input_file_path="input")
    example = Solution(input_file_path="example")
    print(f"Part one example: {example.part_one()}")
    print(f"Part one: {solution.part_one()}")
    print(f"Part two example: {example.part_two()}")
    print(f"Part two: {solution.part_two()}")
