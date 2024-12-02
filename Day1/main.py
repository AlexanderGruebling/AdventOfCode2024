from collections import Counter

def task_one():
    with open("input.txt", "r") as file:
        input_data = file.readlines()

    list_one = []
    list_two = []

    for row in input_data:
        parts = row.strip().split("   ")
        list_one.append(int(parts[0]))
        list_two.append(int(parts[1]))

    list_one.sort()
    list_two.sort()

    total_distance = sum(abs(a - b) for a, b in zip(list_one, list_two))

    print(total_distance)

def task_two():
    with open("input.txt", "r") as file:
        list_one = []
        list_two_counter = Counter()

        for line in file:
            parts = map(int, line.strip().split("   "))
            x, y = parts
            list_one.append(x)
            list_two_counter[y] += 1

    list_one_counter = Counter(list_one)
    sim_score = sum(item * list_two_counter[item] for item in list_one_counter)

    print(sim_score)


task_one()
task_two()