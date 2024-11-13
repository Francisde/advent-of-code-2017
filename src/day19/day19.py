def solvePartOne(inputFild):
    direction = "DOWN"
    currentX = 0
    currentY = 0
    readWord = ""
    for i in range(len(inputFild[0])):
        if inputFild[0][i] == "|":
            currentX = i
            break
    # simulate
    step = 0
    while True:
        print("step: {}, x: {}, y: {}, current sign: {}, direction: {}".format(step, currentX, currentY, inputFild[currentY][currentX], direction))
        # input("??")
        step += 1
        if inputFild[currentY][currentX] == " ":
            return (readWord, step -1)
        if inputFild[currentY][currentX] == "|":
            if direction == "DOWN":
                currentY += 1
            if direction == "UP":
                currentY -= 1
            if direction == "RIGHT":
                currentX += 1
            if direction == "LEFT":
                currentX -= 1
            continue
        if inputFild[currentY][currentX] == "-":
            if direction == "DOWN":
                currentY += 1
            if direction == "UP":
                currentY -= 1
            if direction == "RIGHT":
                currentX += 1
            if direction == "LEFT":
                currentX -= 1
            continue
        if inputFild[currentY][currentX] == "+":
            if direction == "DOWN" or direction == "UP":
                if inputFild[currentY][currentX - 1] != " ":
                    direction = "LEFT"
                    currentX -= 1
                elif inputFild[currentY][currentX + 1] != " ":
                    direction = "RIGHT"
                    currentX += 1
            elif direction == "LEFT" or direction == "RIGHT":
                if currentY + 1 < len(inputFild) and inputFild[currentY + 1][currentX] != " ":
                    direction = "DOWN"
                    currentY += 1
                elif inputFild[currentY - 1][currentX] != " ":
                    direction = "UP"
                    currentY -= 1
            continue
        if inputFild[currentY][currentX].isalpha():
            readWord += inputFild[currentY][currentX]
            if direction == "DOWN":
                currentY += 1
            if direction == "UP":
                currentY -= 1
            if direction == "RIGHT":
                currentX += 1
            if direction == "LEFT":
                currentX -= 1
            continue



def print2D(inputField):
    for row in inputField:
        print(row)
file1 = open('puzzle19.txt', 'r')
Lines = file1.readlines()

count = 0

field = []
max_length = 0
for line in Lines:
    input_line= line.replace("\n", "")
    print("Line {}: {}".format(count, input_line))
    field.append(list(input_line))
    max_length = max(max_length, len(list(input_line)))
    count += 1

for row in field:
    if len(row) < max_length:
        diff = max_length - len(row)
        for i in range(diff):
            row.append(" ")

print2D(field)

print("TASK 1 - solution: {}".format(solvePartOne(field)[0]))

print("TASK 2 - solution: {}".format(solvePartOne(field)[1]))
