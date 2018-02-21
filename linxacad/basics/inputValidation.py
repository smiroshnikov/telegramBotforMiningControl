def validate_user_input(user_data):
    result = False
    for e in user_data:
        if (not e.isdigit()) or (e == '0'):
            print("Only positive numbers are allowed !, try again ")
            break
        else:
            result = True
    return result


def get_user_data(required_parameters):
    for p in required_parameters:
        while True:
            p = input(f"Please enter value ")
            validate_user_input(p)
            if validate_user_input(p):
                break


weight, height, units = None, None, None
rp = [weight, height, units]
get_user_data(rp)
print(rp)
