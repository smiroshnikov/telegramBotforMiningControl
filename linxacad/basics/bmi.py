#!bin/python


def get_user_data():
    height = input("Whats your height :? (inches or meters) ")

    weight = input("Whats your weight :? (pounds or kilograms) ")
    unit = input("Are your measurements in metric or imperial units ? ").lower().strip()
    return weight, height, unit


def calculate_bmi(weight, height, unit="metric"):
    if unit == "metric":
        bmi = (float(weight / (height) ** 2))
    else:
        bmi = 703 * (float(weight / (height ** 2)))
    return bmi


while True:
    height, weight, unit = get_user_data()

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
