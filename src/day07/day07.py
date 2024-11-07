class Program:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.programs_on_top = []

    def add_program_on_top(self, program):
        self.programs_on_top.append(program)

    def get_total_weight(self):
        if len(self.programs_on_top) == 0:
            return self.weight
        else:
            total_weight = self.weight
            for program in self.programs_on_top:
                total_weight += program.get_total_weight()
            return total_weight

    def is_balanced(self):
        if len(self.programs_on_top) == 0:
            return True
        else:
            result = True
            weights_on_top = []
            for program in self.programs_on_top:
                weights_on_top.append(program.get_total_weight())
            weights_set = set(weights_on_top)
            if len(weights_set) != 1:
                return False
            else:
                return True

def solve_part_one(input_list):
    for program in input_list:
        sub_program = False
        for program2 in input_list:
            if program in program2.programs_on_top:
                sub_program = True
        if not sub_program:
            return program

    return "error"

def solve_part_two(input_list):
    wrong_counter = 0
    for program in input_list:

        # print("program: {}, is balanced: {}".format(program.name, program.is_balanced()))
        if not program.is_balanced():
            wrong_counter += 1
            top_most = True
            for sub_program in program.programs_on_top:
                if not sub_program.is_balanced():
                    top_most = False
            if top_most:
                weight_list = []
                for sub_program in program.programs_on_top:
                    weight_list.append(sub_program.get_total_weight())
                    print("total weight {}, single weight {}".format(sub_program.get_total_weight(), sub_program.weight))
                print(weight_list)
    print("wrongcounter {}".format(wrong_counter))



file1 = open('puzzle07.txt', 'r')
Lines = file1.readlines()

count = 0
program_list = []

# parse programs
for line in Lines:
    input_line= line.strip()
    split_line = input_line.split(" ")
    weight = split_line[1].replace("(", "")
    weight = weight.replace(")", "")
    program_list.append(Program(split_line[0], int(weight)))

# add subprograms
for line in Lines:
    input_line= line.strip()
    if " -> " in input_line:
        root_program  = input_line.split(" -> ")[0]
        root_program = root_program.split(" ")[0]
        top_programs = input_line.split(" -> ")[1]
        root_p = None
        for program in program_list:
            if program.name == root_program:
                root_p = program
        for program in program_list:
            if program.name in top_programs.split(", "):
                root_p.add_program_on_top(program)


print("Total number of programs: {}".format(len(program_list)))

print("TASK 1 - bottom program: {} ".format(solve_part_one(program_list).name))

solve_part_two(program_list)
print("TASK 2 - ")
