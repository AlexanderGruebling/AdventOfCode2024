import re

def task_one(instructions):
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instructions)

    total_sum = sum(int(x) * int(y) for x, y in matches)

    print(total_sum)

def task_two(instructions):
    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", instructions)
    
    total_sum = 0
    execute_mode = True

    for instruction in matches:
        if instruction == "don't()":
            execute_mode = False
        elif instruction == "do()":
            execute_mode = True
        elif instruction.startswith("mul") and execute_mode:
            x, y = map(int, re.findall(r"\d{1,3}", instruction))
            total_sum += x * y
    
    print(total_sum)

with open("input.txt", "r") as file:
    instructions = file.read()

task_one(instructions)
task_two(instructions)
