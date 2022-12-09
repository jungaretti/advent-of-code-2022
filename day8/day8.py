"""
O(n^2) solution for Advent of Code 2022 day 2
"""

from enum import Enum

class Direction(Enum):
    """Direction relative to the tree"""
    TOP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

def distance_visible(trees: list[int], height: int) -> int:
    """Finds the distance of the furthest visible tree"""
    for index, tree in enumerate(trees):
        if tree >= height:
            return index+1
    return len(trees)

def memoize_distances(forest: list[list[int]]) -> list[list[dict[int,(int, int, int, int)]]]:
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
            neighbors[Direction.TOP] = distance_visible(top, height)
            neighbors[Direction.RIGHT] = distance_visible(right, height)
            neighbors[Direction.DOWN] = distance_visible(down, height)
            neighbors[Direction.LEFT] = distance_visible(left, height)

            new_row.append(neighbors)
        solution.append(new_row)
    return solution

def part_two(filename: str) -> int:
    """Memoizes distances and finds the greatest scenic score"""
    lines: list[str] = []
    with open(filename, "r", encoding="UTF-8") as file:
        lines = file.read().splitlines()

    forest = []
    for line in lines:
        new_row = []
        for tree in line:
            new_row.append(tree)
        forest.append(new_row)

    key = memoize_distances(forest)

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

print("P2", "test", part_two("day8-test.txt"))
print("P2", part_two("day8.txt"))
