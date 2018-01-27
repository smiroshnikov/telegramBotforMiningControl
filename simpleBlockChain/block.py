import json
import os


def main():
    write_block_to_file("Kozel Petrovich", 10, "Ivan Ivanov", "1111111")


def write_block_to_file(name, amount, recipient, previous_hash=''):
    blockchain_dir = os.curdir + '/blockchain/'

    files_in_folder = os.listdir(blockchain_dir)

    """
    if i want to use numeric convention for block files , i have to sort it after converting file name to int
    if i decide to go with strings , then wrapping in sorted should do
    """
    # print(files_in_folder)
    # print("files are sorted")
    # print(sorted(files_in_folder))
    """
    for now I decided to go numerical 
    """
    files_in_folder = sorted([int(i) for i in files_in_folder])
    print (files_in_folder)

    # data = {"name": name,
    #         "amount": amount,
    #         "recipient": recipient,
    #         "hash": previous_hash
    #         }
    #
    # with open(blockchain_dir + "test", "w") as block_file:
    #     json.dump(data, block_file, indent=4, ensure_ascii=False)
    #


if __name__ == '__main__':
    # if executed via console , executes main
    # if block.py will be imported, main() will not be executed
    main()
