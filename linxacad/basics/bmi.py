#!bin/python

def validate_input(input):
    for e in input:
        if not e.isdigit():
            print("only digit input allowed  :")
            return False
        else:
            return True


def get_user_data():
    height = input("Whats your height :? (inches or meters) ")
    while not validate_input(height):
        print("Please use a numeric value...")
        height = input("Whats your height :? (inches or meters) ")
        validate_input(height)



    weight = input("Whats your weight :? (pounds or kilograms) ")
    unit = input("Are your measurements in metric or imperial units ? ").lower().strip()
    return weight, height, unit, stop_flag


def calculate_bmi(weight, height, unit="metric"):
    if unit == "metric":
        bmi = (float(weight / (height) ** 2))
    else:
        bmi = 703 * (float(weight / (height ** 2)))
    return bmi


stop_flag = False

while not stop_flag:
    height, weight, unit, stop_flag = get_user_data()
    if stop_flag:
        break

    if (unit.lower().startswith("q") or
            weight.lower().startswith("q") or
            height.lower().startswith("q")):
        print("Quiting ....")
        break
    elif unit.startswith("i"):
        print(f"Your BMI is {calculate_bmi(height=height, weight=weight, unit='imperial')}")
    elif unit.startswith("m"):
        print(f"Your BMI is {calculate_bmi(height=height, weight=weight, unit='metric')}")

    else:
        print(f"Unsupported format {unit}, FU!")
