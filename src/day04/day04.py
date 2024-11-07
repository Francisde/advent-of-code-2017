from http.cookiejar import join_header_words


def number_of_valid_passphrases_part_1(input_list):
    valid = 0
    for passphrase in input_passphrases:
        words = passphrase.split(" ")
        word_set = set(words)
        if len(word_set) == len(words):
            valid += 1
    return valid

def number_of_valid_passphrases_part_2(input_list):
    valid = 0
    for passphrase in input_passphrases:
        words = passphrase.split(" ")
        found_anagram = False
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if is_anagram(words[i], words[j]):
                        found_anagram = True
        if found_anagram == False:
            valid += 1
        # print("{}, valid: {}".format(passphrase, not found_anagram))
    return valid

def is_anagram(word1, word2):
    letters1 = list(word1)
    letters1.sort()
    letters2 = list(word2)
    letters2.sort()
    if letters1 == letters2:
        return True
    return False


file1 = open('puzzle04.txt', 'r')
Lines = file1.readlines()

count = 0

input_passphrases = []
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    input_passphrases.append(input_line)


print("TASK 1 - {}".format(number_of_valid_passphrases_part_1(input_passphrases)))

print("TASK 2 - {}".format(number_of_valid_passphrases_part_2(input_passphrases)))
