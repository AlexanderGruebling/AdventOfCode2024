from enum import Enum
from typing import List


class Direction(Enum):
    BOTTOM_LEFT_TO_TOP_RIGHT = 1
    TOP_LEFT_TO_BOTTOM_RIGHT = 2


def count_word_in_string(string: str, word: str) -> int:
    return string.count(word)


def transpose(grid: List[str]) -> List[str]:
    return ["".join(row[col] for row in grid) for col in range(len(grid[0]))]


def extract_diagonals(grid: List[str], direction: Direction) -> List[str]:
    rows, cols = len(grid), len(grid[0])
    diagonals = []

    if direction == Direction.TOP_LEFT_TO_BOTTOM_RIGHT:
        for diag in range(rows + cols - 1):
            diagonals.append("".join(
                grid[i][diag - i] for i in range(max(0, diag - cols + 1), min(diag + 1, rows))
            ))
    elif direction == Direction.BOTTOM_LEFT_TO_TOP_RIGHT:
        for diag in range(rows + cols - 1):
            diagonals.append("".join(
                grid[rows - 1 - i][diag - i] for i in range(max(0, diag - cols + 1), min(diag + 1, rows))
            ))

    return diagonals


def search_horizontally(grid: List[str], word: str) -> int:
    return sum(count_word_in_string(row, word) for row in grid)


def search_vertically(grid: List[str], word: str) -> int:
    transposed_grid = transpose(grid)
    return search_horizontally(transposed_grid, word)


def search_diagonally(grid: List[str], direction: Direction, word: str) -> int:
    diagonals = extract_diagonals(grid, direction)
    return search_horizontally(diagonals, word)


def search_word(grid: List[str], word: str) -> int:
    return (
        search_horizontally(grid, word) +
        search_vertically(grid, word) +
        search_diagonally(grid, Direction.TOP_LEFT_TO_BOTTOM_RIGHT, word) +
        search_diagonally(grid, Direction.BOTTOM_LEFT_TO_TOP_RIGHT, word)
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        grid = f.read().splitlines()

    xmas = search_word(grid, "XMAS")
    samx = search_word(grid, "SAMX")

    print(xmas + samx)
