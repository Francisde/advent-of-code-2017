def solve_part_one(lines_list):
    result = 0
    for line in lines_list:
        current_line = line.strip()
        current_line = current_line.replace("\t", " ")
        min_number = -1
        max_number = -1
        for number in current_line.split(" "):
            int_number = int(number)
            if min_number == -1:
                min_number = int_number
                max_number = int_number
            else:
                min_number = min(min_number, int_number)
                max_number = max(max_number, int_number)
        result += (max_number - min_number)
    return result

def solve_part_two(lines_list):
    result = 0
    for line in lines_list:
        current_line = line.strip()
        current_line = current_line.replace("\t", " ")
        int_numbers = [int(x) for x in current_line.split(" ") ]
        print(int_numbers)
        for number_1 in int_numbers:
            for number_2 in int_numbers:
                if number_1 != number_2:
                    if number_1 % number_2 == 0:
                        result += number_1 // number_2
    return result



file1 = open('puzzle02.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1

result_one = solve_part_one(Lines)
result_two = solve_part_two(Lines)

print("TASK 1 - result: {}".format(result_one))

print("TASK 2 - result: {}".format(result_two))
