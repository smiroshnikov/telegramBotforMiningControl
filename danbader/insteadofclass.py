from collections import namedtuple

"""
Can be used as enums or structs , something simple
also immutable
"""

Account = namedtuple('Account', 'id firstname lastname dob')

ym = Account((123123, 1212), 'test2', 'test3', '18/18/2018')

print(ym)
print(ym.count('test'))
print(ym.count('test2'))

print(ym.index('test3', 0, 4))

import schedule
import time

exit_flag = True


def job(n):
    global glob_exit_flag  # just testing globals
    print(f"Passed arg is job...n is {n}")
    glob_exit_flag = False


"""
will be executed only once per 6 seconds 
"""

schedule.every(3).seconds.do(job, "*ARGS")

n = 0
while 1:
    schedule.run_pending()
    time.sleep(1)
    n += 1
    print(n)
    if n > 10  or not exit_flag:
        break
