class DoubleLinkedNode:

    def __init__(self, value):
        self.value = value
        self.nodeBefore = self
        self.nodeAfter = self

class LoopList:

    def __init__(self, length):
        self.length = length
        self.startNode = None
        self.lastNode = None

    def generateList(self):
        self.startNode = DoubleLinkedNode(0)
        self.lastNode = self.startNode
        for i in range(1, self.length):
            newNode = DoubleLinkedNode(i)
            self.addNodeToEnd(newNode)

    def addNodeToEnd(self, node):
        node.nodeAfter = self.startNode
        self.lastNode.nodeAfter = node
        node.nodeBefore = self.lastNode
        self.lastNode = node

    def perform_reverse(self, start, length):
        helper_list = []
        current_node = self.startNode
        for i in range(start):
            current_node = current_node.nodeAfter
        start_position = current_node
        subNode = current_node
        for i in range(length):
            helper_list.append(subNode.value)
            subNode = subNode.nodeAfter
        helper_list.reverse()
        for i in range(length):
            start_position.value = helper_list[i]
            start_position = start_position.nodeAfter

    def get_solution_one(self):
        result = self.startNode.value * self.startNode.nodeAfter.value
        return result

    def get_dense_hash(self):
        result_list = []
        result_hash = ""
        current_node =self.startNode
        for i in range(16):
            result = 0
            for j in range(16):
                result = result ^ current_node.value
                current_node = current_node.nodeAfter
            result_list.append(result)

        return ''.join(format(x, '02x') for x in result_list)



    def __repr__(self):
        result = "[" + str(self.startNode.value)
        newNode = self.startNode.nodeAfter
        while newNode != self.startNode:
            result = result + ", " + str(newNode.value)+ " "
            newNode = newNode.nodeAfter
        result += "]"
        return result

def get_knot_hash(input_value):
    list_end = [17, 31, 73, 47, 23]
    input_lengths = []
    input_line= input_value.strip()
    for character in input_line:
        # print("Character: {}, ord(): {}".format(character, ord(character)))
        input_lengths.append(ord(character))
    input_lengths += list_end
    loopList = LoopList(256)
    loopList.generateList()

    current_position = 0
    skip_size = 0
    for i in range(64):
        # print("round: {}".format(i))
        for length_value in input_lengths:
            # print("perform length: {} on list {}, current postition: {}".format(length_value, loopList, current_position))
            loopList.perform_reverse(current_position, length_value)
            current_position += (length_value + skip_size) % 256
            skip_size += 1
            # print("result list {}".format(loopList))
    return loopList.get_dense_hash()

if __name__ == "__main__":

    file1 = open('test.txt', 'r')
    Lines = file1.readlines()

    input_lengths = []
    for line in Lines:
        input_line= line.strip()
        input_split = input_line.split(",")


    loopList = LoopList(256)
    loopList.generateList()
    print(input_lengths)



    current_position = 0
    skip_size = 0
    for length_value in input_lengths:
        # print("perform length: {} on list {}, current postition: {}".format(length_value, loopList, current_position))
        loopList.perform_reverse(current_position, length_value)
        current_position += (length_value + skip_size)
        skip_size += 1
        # print("result list {}".format(loopList))

    print("TASK 1 - Check {}".format(loopList.get_solution_one()))
    list_end = [17, 31, 73, 47, 23]
    input_lengths = []
    for line in Lines:
        input_line= line.strip()
        for character in input_line:
            print("Character: {}, ord(): {}".format(character, ord(character)))
            input_lengths.append(ord(character))
    input_lengths += list_end
    loopList = LoopList(256)
    loopList.generateList()
    print(input_lengths)

    current_position = 0
    skip_size = 0
    for i in range(64):
        # print("round: {}".format(i))
        for length_value in input_lengths:
            # print("perform length: {} on list {}, current postition: {}".format(length_value, loopList, current_position))
            loopList.perform_reverse(current_position, length_value)
            current_position += (length_value + skip_size) % 256
            skip_size += 1
            # print("result list {}".format(loopList))
    print(loopList)
    print(loopList.get_dense_hash())

    print("TASK 2 - ")