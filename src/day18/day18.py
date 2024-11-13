class Program:

    def __init__(self, id, instruction_list):
        self.id = id
        self.registers = dict()
        self.registers["p"] = id
        self.incoming_queue = []
        self.instruction_pointer = 0
        self.instruction_list = instruction_list
        self.other_program = None
        self.values_send = 0

    def set_other_program(self ,other):
        self.other_program = other

    def get_next_input(self):
        if len(self.incoming_queue) == 0:
            return None
        else:
            return self.incoming_queue.pop()

    def perform_steps_until_block(self):
        while True:
            instruction = self.instruction_list[self.instruction_pointer]
            # print("instruction_pointer {}, instruction: {}".format(self.instruction_pointer, instruction))
            # input("next")
            if instruction.startswith("snd"):
                split_instruction = instruction.split(" ")
                self.other_program.incoming_queue.append(get_instruction_value(split_instruction[1], self.registers))
                self.values_send +=1
            if instruction.startswith("rcv"):
                split_instruction = instruction.split(" ")
                next_value = self.get_next_input()
                if next_value == None:
                    return
                else:
                    self.registers[split_instruction[1]] = next_value
            if instruction.startswith("set"):
                split_instruction = instruction.split(" ")
                self.registers[split_instruction[1]] = get_instruction_value(split_instruction[2], self.registers)
            if instruction.startswith("add"):
                split_instruction = instruction.split(" ")
                if split_instruction[1] in self.registers:
                    self.registers[split_instruction[1]] += get_instruction_value(split_instruction[2], self.registers)
                else:
                    self.registers[split_instruction[1]] = get_instruction_value(split_instruction[2], self.registers)
            if instruction.startswith("mul"):
                split_instruction = instruction.split(" ")
                if split_instruction[1] in self.registers:
                    self.registers[split_instruction[1]] *= get_instruction_value(split_instruction[2], self.registers)
                else:
                    self.registers[split_instruction[1]] = 0
            if instruction.startswith("mod"):
                split_instruction = instruction.split(" ")
                if split_instruction[1] in self.registers:
                    self.registers[split_instruction[1]] = self.registers[split_instruction[1]] % get_instruction_value(split_instruction[2], self.registers)
                else:
                    self.registers[split_instruction[1]] = 0
            if instruction.startswith("jgz"):
                # print("register i: {}".format(self.registers["i"]))
                split_instruction = instruction.split(" ")
                if split_instruction[1] in self.registers:
                    if self.registers[split_instruction[1]] != 0:
                        self.instruction_pointer = self.instruction_pointer + get_instruction_value(split_instruction[2], self.registers)
                        # print("new instruction pointer: {}".format(self.instruction_pointer))
                    else:
                        self.instruction_pointer += 1
                else:
                    self.registers[split_instruction[1]] = 0
                    self.instruction_pointer += 1
            else:
                self.instruction_pointer += 1
            if self.instruction_pointer >= len(instructions):
                print("error")
                return


def solve_part_one(instructions_list, registers_dict):
    instruction_pointer = 0

    while True:
        instruction = instructions_list[instruction_pointer]
        print("instruction_pointer {}, instruction: {}".format(instruction_pointer, instruction))

        # input("next")
        if instruction.startswith("snd"):
            split_instruction = instruction.split(" ")
            last_sounds[split_instruction[1]] = registers[split_instruction[1]]
        if instruction.startswith("rcv"):
            split_instruction = instruction.split(" ")
            if last_sounds[split_instruction[1]] != 0:
                return last_sounds[split_instruction[1]]
        if instruction.startswith("set"):
            split_instruction = instruction.split(" ")
            registers[split_instruction[1]] = get_instruction_value(split_instruction[2], registers_dict)
        if instruction.startswith("add"):
            split_instruction = instruction.split(" ")
            if split_instruction[1] in registers:
                registers[split_instruction[1]] += get_instruction_value(split_instruction[2], registers_dict)
            else:
                registers[split_instruction[1]] = get_instruction_value(split_instruction[2], registers_dict)
        if instruction.startswith("mul"):
            split_instruction = instruction.split(" ")
            if split_instruction[1] in registers:
                registers[split_instruction[1]] *= get_instruction_value(split_instruction[2], registers_dict)
            else:
                registers[split_instruction[1]] = 0
        if instruction.startswith("mod"):
            split_instruction = instruction.split(" ")
            if split_instruction[1] in registers:
                registers[split_instruction[1]] = registers[split_instruction[1]] % get_instruction_value(split_instruction[2], registers_dict)
            else:
                registers[split_instruction[1]] = 0
        if instruction.startswith("jgz"):
            print("register i: {}".format(registers["i"]))
            split_instruction = instruction.split(" ")
            if split_instruction[1] in registers:
                if registers[split_instruction[1]] != 0:
                    instruction_pointer = instruction_pointer + get_instruction_value(split_instruction[2], registers_dict)
                    print("new instruction pointer: {}".format(instruction_pointer))
                else:
                    instruction_pointer += 1
            else:
                registers[split_instruction[1]] = 0
                instruction_pointer += 1
        else:
            instruction_pointer += 1
        if instruction_pointer >= len(instructions):
            break


def solve_part_two(instructions_list):
    program1 = Program(0, instructions_list)
    program2 = Program(1, instructions_list)
    program1.set_other_program(program2)
    program2.set_other_program(program1)
    program1.perform_steps_until_block()
    while True:

        program1.perform_steps_until_block()
        program2.perform_steps_until_block()
        if len(program1.incoming_queue) == 0 and len(program2.incoming_queue) == 0:
            return program2.values_send


def get_instruction_value(input, registers_dict):
    test = input
    test = test.replace("-","")
    if test.isdecimal():
        return int(input)
    else:
        if input in registers_dict:
            return registers_dict[input]
        else:
            registers_dict[input] = 0
            return 0


file1 = open('puzzle18.txt', 'r')
Lines = file1.readlines()

count = 0

registers = dict()
last_sounds = dict()
last_sounds["a"] = 0
last_sounds["b"] = 0
instructions = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    instructions.append(input_line)
    count += 1



print("TASK 1 - last Played sound: {}".format(solve_part_one(instructions, registers)))

print("TASK 2 - values send: {}".format(solve_part_two(instructions)))
