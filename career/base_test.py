import string

print(string.ascii_lowercase[::-1])

with open('sowpods.txt') as f:  # diffrence between using file and with
    lines = f.readlines()
    lines = [line for line in lines]  # convert lines into string
    print(len(lines))


def count_words_that_start_with_letter(word_list, letter='A'):
    required_letter_count = 0
    for line in word_list:
        if line.startswith(letter):
            required_letter_count += 1
    print("there are " + str(required_letter_count) + " words that start with '" + letter + "'")
    return required_letter_count


def check_if_any_double_letter_exist(word_list):
    creepy_word_list = []

    for letter in string.ascii_lowercase:
        exists = False
        for word in word_list:
            if letter * 2 in word_list:
                exists = True
                creepy_word_list.append(word)
        if not exists:
            print("there are no english words with double " + letter)
    return creepy_word_list


count_words_that_start_with_letter(lines, 'Z')
print (check_if_any_double_letter_exist(lines))

# with will close the file block


# reverse an abc
# for letter in string.ascii_lowercase:
#     print(letter)
