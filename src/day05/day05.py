def solve_part_one(instruction_list):
    steps = 0
    current_instruction = 0
    while current_instruction < len(instruction_list):
        old_index = current_instruction
        current_instruction = current_instruction + instruction_list[old_index]
        instruction_list[old_index] += 1
        steps += 1
    return steps

def solve_part_two(instruction_list):
    steps = 0
    current_instruction = 0
    while current_instruction < len(instruction_list):
        old_index = current_instruction
        current_instruction = current_instruction + instruction_list[old_index]
        if instruction_list[old_index] >=3:
            instruction_list[old_index] -= 1
        else:
            instruction_list[old_index] += 1
        steps += 1
    return steps


file1 = open('puzzle05.txt', 'r')
Lines = file1.readlines()

count = 0

instructions = []

for line in Lines:
    input_line= line.strip()
    instructions.append(int(input_line))



print("TASK 1 - Steps: {}".format(solve_part_one(instructions.copy())))

print("TASK 2 - Steps: {}".format(solve_part_two(instructions)))
