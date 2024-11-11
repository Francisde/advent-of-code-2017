from src.day10.day10 import LoopList, get_knot_hash

def build_grid(seed):
    grid = []
    for i in range(128):
        print(i)
        hash_value = get_knot_hash(seed + "-{}".format(i))
        bin_string = ""
        for character in hash_value:
            bin_string += hex_dict[character]
        line = []
        for character in bin_string:
            if character == "1":
                line.append(-1)
            else:
                line.append(0)
        grid.append(line)
    return grid

def find_all_regions(grid):
    index = 1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == -1:
                mark_region_rec(grid, j, i, index)
                index += 1

def mark_region_rec(grid, start_x, start_y, marker):
    grid[start_y][start_x] = marker
    if start_y < len(grid) - 1:
        if grid[start_y + 1][start_x] == -1:
            mark_region_rec(grid, start_x, start_y + 1, marker)
    if start_y > 0:
        if grid[start_y - 1][start_x] == -1:
            mark_region_rec(grid, start_x, start_y - 1, marker)
    if start_x < len(grid) - 1:
        if grid[start_y][start_x + 1] == -1:
            mark_region_rec(grid, start_x + 1, start_y, marker)
    if start_x > 0:
        if grid[start_y][start_x - 1] == -1:
            mark_region_rec(grid, start_x - 1, start_y, marker)

def solve_part_one(grid):
    used_squares = 0
    for row in grid:
        for character in row:
            if character == -1:
                used_squares += 1
    return used_squares

def solve_part_two(grid):
    max_region = 0
    find_all_regions(grid)
    for row in grid:
        for character in row:
            max_region = max(max_region, character)
    return max_region


hex_dict = dict()
hex_dict["0"] = "0000"
hex_dict["1"] = "0001"
hex_dict["2"] = "0010"
hex_dict["3"] = "0011"
hex_dict["4"] = "0100"
hex_dict["5"] = "0101"
hex_dict["6"] = "0110"
hex_dict["7"] = "0111"
hex_dict["8"] = "1000"
hex_dict["9"] = "1001"
hex_dict["a"] = "1010"
hex_dict["b"] = "1011"
hex_dict["c"] = "1100"
hex_dict["d"] = "1101"
hex_dict["e"] = "1110"
hex_dict["f"] = "1111"

# puzzle_input = "flqrgnkx"
puzzle_input = "vbqugkhl"

input_lengths = []

complete_grid = build_grid(puzzle_input)


print("TASK 1 - used squares = {}".format(solve_part_one(complete_grid)))

print("TASK 2 - number of regions: {}".format(solve_part_two(complete_grid)))
