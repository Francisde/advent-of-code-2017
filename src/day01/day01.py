
def solve_part_one(input_string):
    result = 0
    for i in range(len(input_string) - 1 ):
        if input_string[i] == input_string[i + 1]:
            result += int(input_string[i])
    if input_string[len(input_string) - 1] == input_string[0]:
        result += int(input_string[0])
    return result

def solve_part_two(input_string):
    distance = len(input_string) // 2
    print(distance)
    result = 0
    for i in range(len(input_string)):
        if input_string[i] == input_string[(i + distance) % len(input_string)]:
            result += int(input_string[i])
    return result

file1 = open('puzzle01.txt', 'r')
Lines = file1.readlines()

count = 0
input_string = ""
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    input_string = input_line
    count += 1


print("TASK 1 - result: {}".format(solve_part_one(input_string)))

print("TASK 2 - result: {}".format(solve_part_two(input_string)))
