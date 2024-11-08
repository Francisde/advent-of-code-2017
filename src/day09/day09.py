def get_score(input_string):
    score = 0
    level = 1
    garbage = False
    garbage_count = 0
    ignore_next = False
    for character in input_string:
        if ignore_next:
            ignore_next = False
            continue
        if garbage and character != '!' and character != '>':
            garbage_count += 1
        if character == '{' and not garbage:
            score  += level
            level += 1
        if character == '}' and not garbage:
            level -= 1
        if character == '<' and not garbage:
            garbage = True
        if character == '>' and garbage:
            garbage = False
        if character == '!' and garbage:
            ignore_next = True


    return score, garbage_count




file1 = open('puzzle09.txt', 'r')
Lines = file1.readlines()

count = 0
puzzle_input = ""

for line in Lines:
    input_line= line.strip()
    puzzle_input = input_line
    print("Line {}: {}, score: {}".format(count, input_line, get_score(input_line)))
    count += 1


print("TASK 1 - Score: {}".format(get_score(puzzle_input)[0]))

print("TASK 2 - Garbage: {}".format(get_score(puzzle_input)[1]))
