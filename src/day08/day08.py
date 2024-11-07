
class Register:

    def __init__(self, name):
        self.name = name
        self.value = 0

def solve_part_one(instruction_list):
    max_value_overall = 0
    for instruction in instruction_list:
        split_instruction = instruction.split(" if ")
        cond_register = split_instruction[1].split(" ")[0]
        cond = split_instruction[1].split(" ")[1]
        cond_value = int(split_instruction[1].split(" ")[2])
        print(cond)
        cond_holds = False
        if cond == ">":
            if registers[cond_register].value > cond_value:
                cond_holds = True
        if cond == ">=":
            if registers[cond_register].value >= cond_value:
                cond_holds = True
        if cond == "<":
            if registers[cond_register].value < cond_value:
                cond_holds = True
        if cond == "<=":
            if registers[cond_register].value <= cond_value:
                cond_holds = True
        if cond == "==":
            if registers[cond_register].value == cond_value:
                cond_holds = True
        if cond == "!=":
            if registers[cond_register].value != cond_value:
                cond_holds = True

        if cond_holds:
            register = split_instruction[0].split(" ")[0]
            opp = split_instruction[0].split(" ")[1]
            opp_value = int(split_instruction[0].split(" ")[2])
            if opp == "dec":
                registers[register].value -= opp_value
            if opp == "inc":
                registers[register].value += opp_value
            max_value_overall = max(max_value_overall, registers[register].value)
    max_value = 0
    for register in register_list:
        max_value = max(max_value, register.value)
    print(max_value_overall)
    return max_value



file1 = open('puzzle08.txt', 'r')
Lines = file1.readlines()

count = 0

register_list = []
registers = dict()
instructions = []
for line in Lines:
    input_line= line.strip()
    instructions.append(input_line)
    print("Line {}: {}".format(count, input_line))
    register_name = input_line.split(" ")[0]
    new_register = Register(register_name)
    registers[register_name] = new_register
    register_list.append(new_register)

    count += 1


print("TASK 1 - max value: {}".format(solve_part_one(instructions)))

print("TASK 2 - ")
