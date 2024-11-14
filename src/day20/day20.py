

class Rule:

    def __init__(self, prefix, suffix):
        self.prefix = prefix
        self.suffix = suffix
        self.prefix_rules = []

    def generate_rules(self):
        prefixes = self.prefix.split("/")
        self.prefix_rules.append(self.prefix)
        self.prefix_rules.append(self.get_flip(prefixes))
        for i in range(4):
            prefixes = self.get_rotate(prefixes)

            self.prefix_rules.append(self.get_prefix_string(prefixes))
            self.prefix_rules.append(self.get_flip(prefixes))

    def match_rule(self, input_string):
        if input_string in self.prefix_rules:
            return True
        else:
            return False


    def get_flip(self, string_list):
        new_list = []
        for line in string_list:
            new_list.append(line[::-1])
        return self.get_prefix_string(new_list)

    def get_rotate(self, string_list):
        return [list(reversed(col)) for col in zip(*string_list)]

    def get_prefix_string(self, string_list):
        if len(string_list) == 2:
            return "{}/{}".format(self.get_string(string_list[0]), self.get_string(string_list[1]))
        else:
            return "{}/{}/{}".format(self.get_string(string_list[0]), self.get_string(string_list[1]), self.get_string(string_list[2]))

    def get_string(self, list_input):
        result = ""
        for char in list_input:
            result += char
        return result

def print_image(matrix):
    for row in matrix:
        result = ""
        for char in row:
            result += char
        print(result)

    print()

def solve_part_one(matrix, rules_list, max_steps):
    print("start solving part one")
    print_image(matrix)

    for i in range(max_steps):
        new_matrix = []
        if len(matrix) % 2 == 0:
            chunks_per_row = len(matrix)  // 2
            print("divisible by 2")



            for y_chunk in range(chunks_per_row):
                new_chunks = []

                for x_chunk in range(chunks_per_row):
                    prefix_string = ""
                    prefix_string += matrix[(y_chunk * 2)][(x_chunk * 2)]
                    prefix_string += matrix[(y_chunk * 2)][(x_chunk * 2) + 1]
                    prefix_string += "/"
                    prefix_string += matrix[(y_chunk * 2) + 1][(x_chunk * 2)]
                    prefix_string += matrix[(y_chunk * 2) + 1][(x_chunk * 2) + 1]
                    print("prefix string: {}".format(prefix_string))
                    for rule in rules_list:
                        if rule.match_rule(prefix_string):
                            new_matrix_string = rule.suffix
                            new_chunks.append(new_matrix_string)
                            break

                new_small_matrix = generate_matrix_from_string(parse_chucks_together(new_chunks))
                for row in new_small_matrix:
                    new_matrix.append(row)
        elif len(matrix) % 3 == 0:
            chunks_per_row = len(matrix)  // 3
            print("divisible by 3")
            print(chunks_per_row)


            for y_chunk in range(chunks_per_row):
                new_chunks = []

                for x_chunk in range(chunks_per_row):
                    prefix_string = ""
                    prefix_string += matrix[(y_chunk * 3)][(x_chunk * 3)]
                    prefix_string += matrix[(y_chunk * 3)][(x_chunk * 3) + 1]
                    prefix_string += matrix[(y_chunk * 3)][(x_chunk * 3) + 2]
                    prefix_string += "/"
                    prefix_string += matrix[(y_chunk * 3) + 1][(x_chunk * 3)]
                    prefix_string += matrix[(y_chunk * 3) + 1][(x_chunk * 3) + 1]
                    prefix_string += matrix[(y_chunk * 3) + 1][(x_chunk * 3) + 2]
                    prefix_string += "/"
                    prefix_string += matrix[(y_chunk * 3) + 2][(x_chunk * 3)]
                    prefix_string += matrix[(y_chunk * 3) + 2][(x_chunk * 3) + 1]
                    prefix_string += matrix[(y_chunk * 3) + 2][(x_chunk * 3) + 2]
                    for rule in rules_list:
                        if rule.match_rule(prefix_string):
                            new_matrix_string = rule.suffix
                            new_chunks.append(new_matrix_string)
                            break
                new_small_matrix = generate_matrix_from_string(parse_chucks_together(new_chunks))
                for row in new_small_matrix:
                    new_matrix.append(row)

        else:
            print("error - not divisible")

        matrix = new_matrix
        print("image after step {}".format(i))
        print_image(matrix)

    result = 0
    for row in matrix:
        for char in row:
            if char == "#":
                result += 1
    return result


def parse_chucks_together(string_list):
    result = ""
    for i in range(len(string_list[0].split("/"))):
        for chunck in string_list:
            result += chunck.split("/")[i]
        result += "/"
    print("result: <{}>".format(result[0:len(result)-1]))
    return result[0:len(result)-1]


def generate_matrix_from_string(input_string):
    matrix = []
    split = input_string.split("/")
    for spl in split:
        matrix.append(list(spl))
    return matrix



start_pic = ".#./..#/###"
rules = []
steps = 18

file1 = open('puzzle20.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    split_line = input_line.split(" => ")
    rule = Rule(split_line[0], split_line[1])
    rule.generate_rules()
    rules.append(rule)

print("TASK 1 - sol: {}".format(solve_part_one(generate_matrix_from_string(start_pic), rules, steps)))

print("TASK 2 - ")
