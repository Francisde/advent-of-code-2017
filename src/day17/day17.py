def solve_part_one(steps, step_size):
    current_position = 0
    buffer = [0]
    for i in range(1, steps):
        new_index = get_new_position(buffer, current_position, step_size)
        current_position = new_index
        buffer.insert(current_position + 1, i)
        current_position += 1
    for i in range(len(buffer)):
        if buffer[i] == 2017:
            return buffer[i + 1 ]
    return buffer

def solve_part_two(steps, step_size):
    current_position = 0
    buffer = [0]
    last_insert_on_one = None
    buffer_length = 1
    for i in range(1, steps):
        new_index = get_new_position_two(buffer_length, current_position, step_size)
        current_position = new_index
        if current_position + 1 == 1:
            last_insert_on_one = i
        current_position += 1
        buffer_length += 1

    return last_insert_on_one


def get_new_position(input_list, current_position, steps):
    new_index = current_position
    if current_position + steps < len(input_list) - 5:
        return current_position + steps
    for i in range(steps):
        if new_index == len(input_list) - 1:
            new_index = 0
        else:
            new_index += 1
    return new_index

def get_new_position_two(input_list_length, current_position, steps):
    new_index = current_position
    if current_position + steps < input_list_length - 5:
        return current_position + steps
    for i in range(steps):
        if new_index == input_list_length - 1:
            new_index = 0
        else:
            new_index += 1
    return new_index


print("TASK 1 - {}".format(solve_part_one(2018,394)))

print("TASK 2 - {}".format(solve_part_two(50000001,394)))
