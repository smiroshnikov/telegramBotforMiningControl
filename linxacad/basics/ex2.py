smiroshnikov = {'admin': True, 'active': True, 'name': "Morbusborbus"}
tmiroshnikov = {'admin': False, 'active': True, 'name': "Dinosavri4ek"}
jmiroshnikov = {'admin': False, 'active': False, 'name': "Rybka"}
ymiroshnikov = {'admin': False, 'active': True, 'name': "Kroka"}


def checkuser(user):
    if user['active'] and user['admin']:
        return (f"ACTIVE - (ADMIN) {user['name']}")
    elif user['admin']:
        return (f"ADMIN {user['name']}")
    if user['active']:
        return (f"ACTIVE {user['name']}")

    elif (not user['active'] or not user['admin']):
        return (f"username {user['name']}")


users = (smiroshnikov, tmiroshnikov, jmiroshnikov, ymiroshnikov)
line = 1
for user in users:
    print(line, ":", checkuser(user))
    # checkuser(user)
    line += 1

my_tuple = (1, 2)
print("%s %s" % my_tuple)
print([1] is [1])
s = {(1, 2): "skjdh"}

print(s[(1, 2)])

print(0 or True)
for x in [1, 2, 3]:
    print(x)
print(not 'Bob')