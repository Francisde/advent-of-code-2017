def solve_part_one(steps, step_size):
    current_position = 0
    buffer = [0]
    for i in range(1, steps):
        if i % 1000000 == 0:
            print(i)
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
    for i in range(1, steps):
        if i % 1000000 == 0:
            print(i/1000000)
        new_index = get_new_position(buffer, current_position, step_size)
        current_position = new_index
        buffer.insert(current_position + 1, i)
        current_position += 1

    return buffer[:5]


def get_new_position(input_list, current_position, steps):
    new_index = current_position
    for i in range(steps):
        if new_index == len(input_list) - 1:
            new_index = 0
        else:
            new_index += 1
    return new_index


print("TASK 1 - {}".format(solve_part_one(2018,394)))

print("TASK 2 - {}".format(solve_part_two(50000001,394)))
