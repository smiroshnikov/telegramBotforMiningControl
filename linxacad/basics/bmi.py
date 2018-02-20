#!bin/python

height = float(input("Whats your height :? (inches or meters) "))
weight = float(input("Whats your weight :? (pounds or kilograms) "))
unit = input("Are your measurements in metric or imperial units ? ".lower().strip())

if unit.startswith("i"):
    bmi = 703 * (weight / (height ** 2))
    print(bmi)
elif unit.startswith("m"):
    bmi = (weight / (height ** 2))
    print(bmi)
else:
    print("unsupported measurements . fuck off")
