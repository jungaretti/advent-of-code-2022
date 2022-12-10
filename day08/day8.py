"""
O(n^2) solution for day 8 part 2
"""

from enum import Enum

class Direction(Enum):
    TOP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

def distance(trees: list[int], height: int) -> int:
    for index, tree in enumerate(trees):
        if tree >= height:
            return index+1
    return len(trees)

def visible(trees: list[int], height: int) -> int:
    for tree in trees:
        if tree >= height:
            return 0
    return 1

def measure(forest: list[list[int]], reducer = lambda _: 0) -> list[list[dict[int,(int, int, int, int)]]]:
    """Finds the distances visible for each tree"""
    solution = []
    for row, _ in enumerate(forest):
        new_row = []
        for col, _ in enumerate(forest[row]):
            top = [i[col] for i in forest][:row]
            down = [i[col] for i in forest][row+1:]
            left = forest[row][:col]
            right = forest[row][col+1:]
            top.reverse()
            left.reverse()

            height = forest[row][col]

            neighbors = {}
            neighbors[Direction.TOP] = reducer(top, height)
            neighbors[Direction.RIGHT] = reducer(right, height)
            neighbors[Direction.DOWN] = reducer(down, height)
            neighbors[Direction.LEFT] = reducer(left, height)

            new_row.append(neighbors)
        solution.append(new_row)
    return solution

def setup(filename: str) -> list[list[int]]:
    lines: list[str] = []
    with open(filename, "r", encoding="UTF-8") as file:
        lines = file.read().splitlines()

    forest = []
    for line in lines:
        new_row = []
        for tree in line:
            new_row.append(tree)
        forest.append(new_row)
    return forest

def part_one(filename: str) -> int:
    forest = setup(filename)
    key = measure(forest, visible)

    solution = 0
    for row, _ in enumerate(forest):
        for col, _ in enumerate(forest[row]):
            top = key[row][col][Direction.TOP]
            down = key[row][col][Direction.DOWN]
            left = key[row][col][Direction.LEFT]
            right = key[row][col][Direction.RIGHT]
            if max(top, down, left, right) == 1:
                solution += 1
    return solution

def part_two(filename: str) -> int:
    forest = setup(filename)
    key = measure(forest, distance)

    solution = -1
    for row, _ in enumerate(forest):
        for col, _ in enumerate(forest[row]):
            top = key[row][col][Direction.TOP]
            down = key[row][col][Direction.DOWN]
            left = key[row][col][Direction.LEFT]
            right = key[row][col][Direction.RIGHT]
            score = top * down * left * right
            solution = max(solution, score)
    return solution

print("P1", "test", part_one("day8-test.txt"))
print("P1", part_one("day8.txt"))
print("P2", "test", part_two("day8-test.txt"))
print("P2", part_two("day8.txt"))
