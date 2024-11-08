def print_field(input_field):
    for row in input_field:
        print(row)

def generate_field_part_one(field_size = 101):
    field = [[0 for x in range(field_size)] for y in range(field_size)]
    current_x = int(field_size / 2)
    current_y = int(field_size / 2)
    current_index = 1
    # init
    field[current_y][current_x] = 1
    field[current_y][current_x + 1] = 2
    field[current_y -1 ][current_x + 1] = 3
    current_y = current_y - 1
    current_x = current_x
    current_index = 4
    direction = 'L'

    while True:
        if current_y < 0 or current_x < 0 or current_x >= field_size or current_y >= field_size:
            break
        field[current_y][current_x] = current_index
        current_index += 1
        if direction == 'L':
            if field[current_y + 1][current_x] != 0:
                current_x -= 1
            else:
                current_y += 1
                direction = 'D'
            continue
        if direction == 'D':
            if field[current_y][current_x + 1] != 0:
                current_y += 1
            else:
                current_x += 1
                direction = 'R'
            continue
        if direction == 'R':
            if field[current_y - 1][current_x] != 0:
                current_x += 1
            else:
                current_y -= 1
                direction = 'U'
            continue
        if direction == 'U':
            if field[current_y][current_x - 1] != 0:
                current_y -= 1
            else:
                current_x -= 1
                direction = 'L'
            continue
    return field

def generate_field_part_two(field_size, search_input):
    field = [[0 for x in range(field_size)] for y in range(field_size)]
    current_x = int(field_size / 2)
    current_y = int(field_size / 2)
    current_index = 1
    # init
    field[current_y][current_x] = 1
    field[current_y][current_x + 1] = 1
    field[current_y -1 ][current_x + 1] = 2
    current_y = current_y - 1
    current_x = current_x
    direction = 'L'

    while True:
        if current_y <= 0 or current_x <= 0 or current_x >= field_size - 1 or current_y >= field_size - 1:
            break
        value_to_save = 0
        value_to_save += field[current_y - 1][current_x]
        value_to_save += field[current_y + 1][current_x]
        value_to_save += field[current_y][current_x + 1]
        value_to_save += field[current_y][current_x - 1]
        value_to_save += field[current_y - 1][current_x + 1]
        value_to_save += field[current_y - 1][current_x - 1]
        value_to_save += field[current_y + 1][current_x + 1]
        value_to_save += field[current_y + 1][current_x - 1]
        if value_to_save > search_input:
            return value_to_save
        field[current_y][current_x] = value_to_save
        current_index += 1
        if direction == 'L':
            if field[current_y + 1][current_x] != 0:
                current_x -= 1
            else:
                current_y += 1
                direction = 'D'
            continue
        if direction == 'D':
            if field[current_y][current_x + 1] != 0:
                current_y += 1
            else:
                current_x += 1
                direction = 'R'
            continue
        if direction == 'R':
            if field[current_y - 1][current_x] != 0:
                current_x += 1
            else:
                current_y -= 1
                direction = 'U'
            continue
        if direction == 'U':
            if field[current_y][current_x - 1] != 0:
                current_y -= 1
            else:
                current_x -= 1
                direction = 'L'
            continue
    return field

def get_distance(input_field, search_value):
    center_x = 0
    center_y = 0
    search_x = 0
    search_y = 0
    # find center
    for y in range(len(input_field)):
        for x in range(len(input_field)):
            if input_field[y][x] == 1:
                center_x = x
                center_y = y
            if input_field[y][x] == search_value:
                search_x = x
                search_y = y
    if search_x == 0:
        return -1
    else:
        return abs(center_x - search_x) + abs(center_y - search_y)




# test
# input = 1024
# size = 5


# puzzle
puzzle_input = 368078
size = 2001

field = generate_field_part_one(size)
result = generate_field_part_two(size, puzzle_input)


print("TASK 1 - Distance: {}".format(get_distance(field, puzzle_input)))

print("TASK 2 - First Value bigger: {}".format(result))
