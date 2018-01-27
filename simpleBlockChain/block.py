import json
import os
import hashlib


def get_hash(filename):
    """
    will open and hash file in binary mode (for better compatibility
    :param filename: filename (block) that is required to be hashed
    :return: hash (md5) of the file
    """
    blockchain_dir = os.curdir + '/blockchain/'
    file = open(blockchain_dir + filename, 'rb').read()
    # return hashlib.sha3_512(file).hexdigest()
    return hashlib.md5(file).hexdigest()


def write_block_to_file(name, recipient, amount, previous_hash=''):
    blockchain_dir = os.curdir + '/blockchain/'
    # converting file names to string and sorting
    files_in_folder = os.listdir(blockchain_dir)
    files_in_folder = sorted([int(i) for i in files_in_folder])
    last_file = files_in_folder[-1]
    next_block_file_name = str(last_file + 1)

    data = {
        "sender": name,
        "recipient": recipient,
        "amount": amount,
        "hash": get_hash(str(last_file))
    }

    with open(blockchain_dir + next_block_file_name, "w") as block_file:
        json.dump(data, block_file, indent=4, ensure_ascii=False)


def main():
    write_block_to_file("Sergey Miroshnikov", "Yana Miroshnikov", 10)


if __name__ == '__main__':
    # if executed via console , executes main
    # if block.py will be imported, main() will not be executed
    main()
