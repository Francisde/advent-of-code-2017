def solve_part_one(input_banks):
    cycles = 0
    seen_configurations = []
    loop_size = 0
    while True:
        index_with_most_blocks = 0
        most_blocks = 0
        for bank in input_banks:
            most_blocks = max(most_blocks, bank)
        print(most_blocks)
        for i in range(len(input_banks)):
            if input_banks[i] == most_blocks:
                index_with_most_blocks = i
                break
        blocks_to_redistribute = input_banks[index_with_most_blocks]
        input_banks[index_with_most_blocks] = 0
        current_index = index_with_most_blocks + 1
        if current_index >= len(input_banks):
            current_index = 0
        while blocks_to_redistribute > 0:
            input_banks[current_index] += 1
            blocks_to_redistribute -= 1
            current_index += 1
            if current_index >= len(input_banks):
                current_index = 0
        cycles += 1
        configuration = get_configuration(input_banks)
        #print("cycle: {}, config: {}".format(cycles, configuration))
        if configuration in seen_configurations:
            loop_size = cycles - seen_configurations.index(configuration)
            print("loop size " + str(loop_size -1))
            break
        else:
            seen_configurations.append(configuration)
    return cycles

def get_configuration(input_banks):
    result = ""
    for bank in input_banks:
        result += "{}-".format(bank)
    return result

file1 = open('puzzle06.txt', 'r')
Lines = file1.readlines()

count = 0

banks = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    blocks_string = input_line.split(" ")
    for block in blocks_string:
        banks.append(int(block))

    count += 1

print("TASK 1 - solution: {}".format(solve_part_one(banks)))

print("TASK 2 - ")
