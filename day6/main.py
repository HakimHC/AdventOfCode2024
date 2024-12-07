import enum
import copy


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class MoveResult(enum.Enum):
    OBJECT = 1
    NOTHING = 2
    OUT_OF_BOUNDS = 3
    ALREADY_STEPPED = 4


class Direction(enum.Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Solution:
    def __init__(self, input_file_path: str = "input"):
        with open(input_file_path, "r") as f:
            self.raw_data = f.read()
        self.map = [list(line) for line in self.raw_data.split("\n") if line]
        self.original_map = self.map.copy()

        self.starting_position = self.__find_starting_position()
        self.max_x = len(self.map[0])
        self.max_y = len(self.map)
        self.current_direction = Direction.UP
        self.current_position = copy.deepcopy(self.starting_position)
        self.directions = [
            Direction.UP,
            Direction.RIGHT,
            Direction.DOWN,
            Direction.LEFT
        ]

    def __is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.max_x and 0 <= y < self.max_y

    def move(self) -> MoveResult:
        self.current_position.x += self.current_direction.value[0]
        self.current_position.y +=  self.current_direction.value[1]
        if not self.__is_in_bounds(self.current_position.x, self.current_position.y):
            return MoveResult.OUT_OF_BOUNDS
        if self.map[self.current_position.y][self.current_position.x] == "#":
            self.current_position.x -= self.current_direction.value[0]
            self.current_position.y -= self.current_direction.value[1]
            return MoveResult.OBJECT
        if self.map[self.current_position.y][self.current_position.x] == "X":
            return MoveResult.ALREADY_STEPPED
        # self.map[self.current_position.y][self.current_position.x] = "X"
        return MoveResult.NOTHING

    def __change_direction(self):
        direction_idx = self.directions.index(self.current_direction)
        direction_idx += 1
        if direction_idx >= len(self.directions):
            direction_idx = 0
        self.current_direction = self.directions[direction_idx]

    def __find_starting_position(self) -> Position:
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == '^':
                    return Position(x, y)

    def part_one(self):
        count = 0
        stop = False
        while not stop:
            step_result = self.move()
            if step_result == MoveResult.OBJECT:
                self.__change_direction()
            elif step_result == MoveResult.OUT_OF_BOUNDS:
                break
            elif step_result == MoveResult.NOTHING:
                count += 1
        for i in self.map:
            print(i)
        return count

    def is_in_loop(self, x: int, y: int) -> bool:
        self.current_position = copy.deepcopy(self.starting_position)
        self.current_direction = Direction.UP
        if x == self.starting_position.x and y == self.starting_position.y:
            return False
        br = sum([len(x) for x in self.map]) * 2
        test = 0
        while test < br:
            test += 1
            res = self.move()
            if res == MoveResult.OBJECT:
                self.__change_direction()
            elif res == MoveResult.OUT_OF_BOUNDS:
                # print("================")
                # for l in self.map:
                #     print(l)
                # print("================")
                return False
        return True

    def part_two(self):
        count = 0
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                self.map = copy.deepcopy(self.original_map)
                self.map[y][x] = "#"
                if self.is_in_loop(x, y):
                    count += 1
                    print(count)
                    # print("=============yy")
                    # for l in self.map:
                    #     print(l)
                    # print("=============yy")
        return count


if __name__ == "__main__":
    solution = Solution(input_file_path="input")
    # example = Solution(input_file_path="example")
    # print(f"Part one example: {example.part_one()}")
    # print(f"Part one: {solution.part_one()}")
    # print(f"Part two example: {example.part_two()}")
    print(f"Part two: {solution.part_two()}")
