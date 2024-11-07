def print_field(input_field):
    for row in input_field:
        print(row)

def generate_field(field_size = 100):
    field = [[0 for x in range(field_size)] for y in range(field_size)]
    current_x = int(field_size / 2)
    current_y = int(field_size / 2)
    current_index = 1
    direction = 'R'
    while True:
        field[current_y][current_x] = current_index
        return field





# test
input = 1

# puzzle
#input = 368078


size = 50

field = generate_field(10)
print_field(field)

print("TASK 1 - ")

print("TASK 2 - ")
