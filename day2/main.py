import copy
from enum import Enum


class Solution:
    def __init__(self, input_file_path: str = "input"):
        with open(input_file_path, "r") as f:
            self.raw_data = f.read()
        self.lines = [line for line in self.raw_data.split("\n") if line]

    @staticmethod
    def is_report_safe(report: list[int]) -> bool:
        i = 1
        operator = ">" if report[0] < report[1] else "<"  # completely unreadable, but i dont care, its easier like this
        while i < len(report):
            diff = abs(report[i] - report[i - 1])
            if not (1 <= diff <= 3) or not (eval(f"report[i] {operator} report[i - 1]")):  # its actually horrible
                return False
            i += 1
        return True

    def part_one(self):
        safe_reports = []
        for line in self.lines:
            report = [int(x) for x in line.strip().split() if x]
            if Solution.is_report_safe(report):
                safe_reports.append(report)
        return len(safe_reports)

    def part_two(self):
        safe_reports = []
        for line in self.lines:
            report = [int(x) for x in line.strip().split() if x]
            for i in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(i)
                if Solution.is_report_safe(report_copy):
                    safe_reports.append(report_copy)
                    break
        return len(safe_reports)


if __name__ == "__main__":
    solution = Solution(input_file_path="input")
    example = Solution(input_file_path="example")
    print(f"Part one example: {example.part_one()}")
    print(f"Part one: {solution.part_one()}")
    print(f"Part two example: {example.part_two()}")
    print(f"Part two: {solution.part_two()}")
