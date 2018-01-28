import json
import os
import hashlib
import filecmp


def get_hash(filename):
    """
    opens and hashes file in binary mode (for better compatibility
    :param filename: filename (block) that is required to be hashed
    :return: string hash(md5) of the file
    """
    blockchain_dir = os.curdir + '/blockchain/'
    file = open(blockchain_dir + filename, 'rb').read()
    # return hashlib.sha3_512(file).hexdigest()
    return hashlib.md5(file).hexdigest()


def write_block_to_file(name, recipient, amount, previous_hash=''):
    """

    :param name: string , Name of a person who sends amount
    :param recipient: string , Name of the recipient
    :param amount: int numeric value
    :param previous_hash: string hex representation of hash
    :return: None
    """

    blockchain_dir = os.curdir + '/blockchain/'
    # converting file names to string and sorting
    files_in_folder = os.listdir(blockchain_dir)
    # list comprehension
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


def check_block_integrity():
    """
    1. Read previous block's hash
    2. Recalculate previous block's hash
    3. Compare 1 and 2
    :return: boolean result

    """
    blockchain_dir = os.curdir + '/blockchain/'
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

    for block_file in files[1:]:
        # first element is not included , hence it has empty hash
        f = open(blockchain_dir + str(block_file))
        file_hash = json.load(f)['hash']
        # к json обращаюсь по ключу
        # print(json.load(open(blockchain_dir + str(block_file)))['hash'])
        # print(json.load(open(blockchain_dir + str(block_file))))
        print(file_hash)
        recalculated_hash = get_hash(str(block_file - 1))
        print(recalculated_hash)
        # return True if recalculated_hash == file_hash else False
        if recalculated_hash != file_hash:
            result = False
            erroneous_block_number = str(block_file)
            print("ERROR! Block number <<" + erroneous_block_number + ">> hash has been ALTERED! ERROR!")
            break
        else:
            result = True
    return result


def main():
    # write_block_to_file("Sergey Miroshnikov", "Yana Miroshnikov", 10)
    # write_block_to_file("Yana Miroshnikov", "Sergey Miroshnikov", 3)
    # write_block_to_file("Sergey Miroshnikov", "Evgeniya Miroshnikov", 1)
    # write_block_to_file("Sergey Miroshnikov", "Alexander Gulbit", 0.5)
    # write_block_to_file("Sergey Miroshnikov", "Dina Gulbit", 1.5)
    print(check_block_integrity())
    s = "abcdef"
    print(s[::-1])


if __name__ == '__main__':
    # if executed via console , executes main
    # if block.py will be imported, main() will not be executed
    main()
