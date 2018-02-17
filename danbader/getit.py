"""
very cool ! :)
"""
user_to_name = {
    123 : "Bob" ,
    2334  : "Kenny",
    11234 : "David"
}

def greeting(uid):
    return "Hey, %s" % user_to_name.get(uid, "DEFAULT")


print(greeting(123))
print(greeting(2215654564)) #no such user !


