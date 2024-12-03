import re

with open("input.txt", "r") as file:
    instructions = file.read()

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instructions)

total_sum = sum(int(x) * int(y) for x, y in matches)

print(total_sum)