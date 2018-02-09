import string

# print(string.ascii_lowercase[::-1])
import threading
import time

start = time.time()

with open('sawpods_small.txt') as f:  # difference between using file and with
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

    for letter in string.ascii_uppercase:
        exists = False
        print("checking letter ..." + letter)
        for word in word_list:
            print("checking " + word)
            if letter * 2 in word:
                exists = True
                creepy_word_list.append(word)
                print("added " + word)
        if not exists:
            print("there are no english words with double " + letter)

    print(str(len(creepy_word_list)) + "total words in list ")
    return creepy_word_list


def run_in_multi():
    t1 = threading.Thread(target=check_if_any_double_letter_exist(lines))
    t2 = threading.Thread(target=check_if_any_double_letter_exist(lines))
    t3 = threading.Thread(target=check_if_any_double_letter_exist(lines))
    t4 = threading.Thread(target=check_if_any_double_letter_exist(lines))
    t5 = threading.Thread(target=check_if_any_double_letter_exist(lines))
    t6 = threading.Thread(target=check_if_any_double_letter_exist(lines))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()


# count_words_that_start_with_letter(lines, 'Z')

print(check_if_any_double_letter_exist(lines))
# run_in_multi()

end = time.time()
print("New time taken for all jobs:", end - start)

# with will close the file block


# reverse an abc
# for letter in string.ascii_lowercase:
#     print(letter)


# i am expected to print :

"""
max words argument == 2 
dick 1900 raz 
penis 3500
hashtable


"""



