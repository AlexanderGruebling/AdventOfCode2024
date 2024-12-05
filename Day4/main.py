from enum import Enum

class Direction(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    TOP_LEFT_TO_BOTTOM_RIGHT = 2
    BOTTOM_LEFT_TO_TOP_RIGHT = 3

def transform(grid, direction):
    if direction == Direction.VERTICAL:
        return ["".join(row[col] for row in grid) for col in range(len(grid[0]))]
    elif direction == Direction.TOP_LEFT_TO_BOTTOM_RIGHT:
        return ["".join(grid[i][d - i] for i in range(max(0, d - len(grid[0]) + 1), min(d + 1, len(grid))))
                for d in range(len(grid) + len(grid[0]) - 1)]
    elif direction == Direction.BOTTOM_LEFT_TO_TOP_RIGHT:
        return ["".join(grid[len(grid) - 1 - i][d - i] for i in range(max(0, d - len(grid[0]) + 1), min(d + 1, len(grid))))
                for d in range(len(grid) + len(grid[0]) - 1)]
    return grid

def search_word(grid, word):
    return sum("".join(row).count(word) for d in Direction for row in transform(grid, d))

with open("input.txt") as f:
    grid = f.read().splitlines()

print(search_word(grid, "XMAS") + search_word(grid, "SAMX"))
