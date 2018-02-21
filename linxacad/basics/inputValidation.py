def validate_user_input(user_data):
    result = False
    for e in user_data:
        if (not e.isdigit()) or (e == '0'):
            print("Only positive numbers are allowed !, try again ")
            break
        else:
            result = True
    return result


height, weight, units = 0, 0, 0
while True:
    height = input("Enter height: ")
    if validate_user_input(height):
        # if validate_user_input(input("Enter Height :")):
        break
