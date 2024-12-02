def validate_list(values):
    if len(values) < 2:
        return True 

    ascending = values[0] <= values[1]

    for i in range(len(values) - 1):
        diff = abs(values[i + 1] - values[i])
        if not (1 <= diff <= 3):
            return False
        if ascending and values[i] > values[i + 1]:
            return False
        if not ascending and values[i] < values[i + 1]:
            return False

    return True

def task_one():
    with open("input.txt", "r") as file:
        num_safe = sum(
            1 for line in file if validate_list(list(map(int, line.split())))
        )
    print(num_safe)

task_one()