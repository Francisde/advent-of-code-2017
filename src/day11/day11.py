def calc_steps(input_list):
    directions = ["n", "s", "ne", "nw", "sw", "se"]
    direction_counter = dict()
    for direction in directions:
        direction_counter[direction] = 0
    for step in input_list:
        direction_counter[step] += 1

    changes = True
    while changes:
        changes = False
        if direction_counter["n"] != 0 and direction_counter["s"] != 0:
            clean_steps = min(direction_counter["n"], direction_counter["s"])
            direction_counter["n"] -= clean_steps
            direction_counter["s"] -= clean_steps
            changes = True
        if direction_counter["ne"] != 0 and direction_counter["sw"] != 0:
            clean_steps = min(direction_counter["ne"], direction_counter["sw"])
            direction_counter["ne"] -= clean_steps
            direction_counter["sw"] -= clean_steps
            changes = True
        if direction_counter["nw"] != 0 and direction_counter["se"] != 0:
            clean_steps = min(direction_counter["nw"], direction_counter["se"])
            direction_counter["nw"] -= clean_steps
            direction_counter["se"] -= clean_steps
            changes = True
        if direction_counter["sw"] != 0 and direction_counter["se"] != 0:
            clean_steps = min(direction_counter["sw"], direction_counter["se"])
            direction_counter["sw"] -= clean_steps
            direction_counter["se"] -= clean_steps
            direction_counter["s"] += clean_steps
            changes = True
        if direction_counter["nw"] != 0 and direction_counter["ne"] != 0:
            clean_steps = min(direction_counter["nw"], direction_counter["ne"])
            direction_counter["nw"] -= clean_steps
            direction_counter["ne"] -= clean_steps
            direction_counter["n"] += clean_steps
            changes = True
        if direction_counter["nw"] != 0 and direction_counter["n"] != 0 and direction_counter["sw"] != 0:
            clean_steps = min(direction_counter["nw"], direction_counter["n"], direction_counter["sw"])
            direction_counter["nw"] -= clean_steps
            direction_counter["sw"] -= clean_steps
            direction_counter["n"] -= clean_steps
            direction_counter["nw"] += (2* clean_steps)
            changes = True
        if direction_counter["nw"] != 0 and direction_counter["s"] != 0 and direction_counter["sw"] != 0:
            clean_steps = min(direction_counter["nw"], direction_counter["s"], direction_counter["sw"])
            direction_counter["nw"] -= clean_steps
            direction_counter["sw"] -= clean_steps
            direction_counter["s"] -= clean_steps
            direction_counter["sw"] += (2* clean_steps)
            changes = True
        if direction_counter["ne"] != 0 and direction_counter["s"] != 0 and direction_counter["se"] != 0:
            clean_steps = min(direction_counter["ne"], direction_counter["s"], direction_counter["se"])
            direction_counter["ne"] -= clean_steps
            direction_counter["se"] -= clean_steps
            direction_counter["s"] -= clean_steps
            direction_counter["se"] += (2* clean_steps)
            changes = True
        if direction_counter["ne"] != 0 and direction_counter["n"] != 0 and direction_counter["se"] != 0:
            clean_steps = min(direction_counter["ne"], direction_counter["n"], direction_counter["se"])
            direction_counter["ne"] -= clean_steps
            direction_counter["se"] -= clean_steps
            direction_counter["n"] -= clean_steps
            direction_counter["se"] += (2* clean_steps)
            changes = True
    result = 0
    for direction in directions:
        result += direction_counter[direction]
    return result



file1 = open('puzzle11.txt', 'r')
Lines = file1.readlines()

count = 0

step_list = []

for line in Lines:
    input_line= line.strip()
    # print("Line {}: {}".format(count, input_line))
    split_line = input_line.split(",")
    for step in split_line:
        step_list.append(step)
    count += 1


print("TASK 1 - Total steps: {}".format(calc_steps(step_list)))


max_steps = 0
for i in range(1, len(step_list)):
    sub_list = step_list[0:i]
    result = calc_steps(sub_list)
    # print(result)
    max_steps = max(max_steps, result)
print("TASK 2 - max_steps: {}".format(max_steps))
