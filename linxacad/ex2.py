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
    print(line ,":", checkuser(user))
    # checkuser(user)
    line += 1
