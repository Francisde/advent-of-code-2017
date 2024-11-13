
def perform_dance(dance_move_list, program_list, repetitions):
    result = ""
    original_list = program_list.copy()
    for j in range(1, repetitions):
        for dance_move in dance_move_list:
            if dance_move.startswith("s"):
                number = int(dance_move[1:])
                program_list = program_list[len(program_list) - number:] + program_list[:len(program_list) - number]
            if dance_move.startswith("x"):
                numbers = dance_move[1:].split("/")
                number1 = int(numbers[0])
                number2 = int(numbers[1])
                char1 = program_list[number1]
                program_list[number1] = program_list[number2]
                program_list[number2] = char1
            if dance_move.startswith("p"):
                programs = dance_move[1:].split("/")
                program1 = programs[0]
                program2 = programs[1]
                index1 = 0
                index2 = 0
                for i in range(len(program_list)):
                    if program_list[i] == program1:
                        index1 = i
                    if program_list[i] == program2:
                        index2 = i
                char1 = program_list[index1]
                program_list[index1] = program_list[index2]
                program_list[index2] = char1

    for program in program_list:
        result += program
    return result


file1 = open('puzzle16.txt', 'r')
Lines = file1.readlines()

count = 0

dance_moves = []

# programs = ["a", "b", "c", "d", "e"]
programs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p"]

for line in Lines:
    input_line= line.strip()
    dance_moves = input_line.split(",")
    count += 1

steps_to_go = 1000000000
new_steps_to_go = 1000000000
while new_steps_to_go > 0:
    steps_to_go = new_steps_to_go
    new_steps_to_go = steps_to_go - 60

print("TASK 1 - final order: {}".format(perform_dance(dance_moves, programs, 1)))

print("TASK 2 - final order: {}".format(perform_dance(dance_moves, programs, steps_to_go + 1)))
