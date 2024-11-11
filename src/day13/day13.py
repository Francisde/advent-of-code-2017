import sys

class Layer:

    def __init__(self, index, depth):
        self.index = index
        self.depth = depth
        self.current_position = 0
        self.direction = "UP"

    def __repr__(self):
        return "Layer {}, current: {}".format(self.index, self.current_position)


    def simulate_one_step(self):
        if self.direction == "UP":
            if self.current_position < self.depth - 1:
                self.current_position += 1
            else:
                self.direction = "DOWN"
                self.current_position -= 1
        elif self.direction == "DOWN":
            if self.current_position > 0:
                self.current_position -= 1
            else:
                self.direction = "UP"
                self.current_position += 1

    def simulate_x_steps(self, x):
        for i in range(x % ((self.depth - 1) * 2)):
            self.simulate_one_step()

    def reset_layer(self):
        self.current_position = 0


def solve_part_one(layer_list, max_simulation):
    severity = 0
    current_position = -1
    for i in range(0, max_simulation + 1):
        # print("second: {}".format(i))
        # for layer in layer_list:
        #     print(layer)
        current_position = i
        if "{}".format(i) in layers_dict:
            if layers_dict["{}".format(i)].current_position == 0:
                severity += (i * layers_dict["{}".format(i)].depth)
        for layer in layer_list:
            layer.simulate_one_step()

    return severity

def solve_part_two(layer_list, max_simulation, min, max):
    delay = min
    while delay < max:
        # print(delay)
        for layer in layer_list:
            layer.reset_layer()
        for layer in layer_list:
            layer.simulate_x_steps(delay)
        if layers_dict["{}".format(0)].current_position != 0:
            sev = solve_part_one(layer_list, max_simulation)
            if sev == 0:
                return delay
        delay += 1


file1 = open('puzzle13.txt', 'r')
Lines = file1.readlines()
layers = []
layers_dict = dict()
max_layer = 0

count = 0

for line in Lines:
    input_line= line.strip()
    split_line = input_line.split(": ")
    newLayer = Layer(split_line[0], int(split_line[1]))
    layers.append(newLayer)
    layers_dict[split_line[0]] = newLayer
    max_layer = int(split_line[0])
    count += 1


print("TASK 1 - severity: {}".format(solve_part_one(layers, max_layer)))

print("TASK 2 - min delay needed: {}".format(solve_part_two(layers, max_layer, 0, 1000000)))


