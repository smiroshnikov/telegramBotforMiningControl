import json


def main():
    write_block_to_file("Kozel Petrovich", 10 , "Ivan Ivanov" , "1111111" )


def write_block_to_file(name, amount, recipient , hash):
    data = {"name": name,
            "amount": amount,
            "recipient": recipient,
            "hash": hash
            }

    with open("test", "w") as block_file:
        json.dump(data, block_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # if executed via console , executes main
    # if block.py will be imported, main() will not be executed
    main()
