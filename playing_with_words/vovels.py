import multiprocessing
import time

vowels = "aeiou"


def has_all_vovels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
        
    return True


if __name__ == "__main__":
    start = time.time()

    with open('words.txt') as f:  # difference between using file and with
        lines = f.readlines()
        lines = [line for line in lines]  # convert lines into string

    pool = multiprocessing.Pool()  # I define separate process for each line
