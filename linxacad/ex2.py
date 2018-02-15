smiroshnikov = {'admin': True, 'active': True, 'name': "Morbusborbus"}
tmiroshnikov = {'admin': False, 'active': True, 'name': "Dinosavri4ek"}
jmiroshnikov = {'admin': False, 'active': False, 'name': "Rybka"}


def checkuser(user):
    if user['admin']:
        print(f"ADMIN {user['name']}")
    if user['active']:
        print(f"ACTIVE {user['name']}")
    if user['active'] and user['admin']:
        print(f"ACTIVE - (ADMIN) {user['name']}")
    elif (not user['active'] or not user['admin']):
        print(f"username {user['name']}")
    print("Done----------------------------\n")


users = (smiroshnikov, tmiroshnikov, jmiroshnikov)

for user in users:
    checkuser(user)
