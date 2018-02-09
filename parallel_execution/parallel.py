import collections
from pprint import pprint
import multiprocessing

import time

import os

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])

scientists = {
    Scientist(name='Morbus Borbus', field='CS', born=1979, nobel=True),
    Scientist(name='Yana Borbus', field='Chemistry', born=1983, nobel=True),
    Scientist(name='Alex Gulbit', field='Math', born=1979, nobel=True),
    Scientist(name='Dina Gulbit', field='Phy', born=1979, nobel=True),
    Scientist(name='Tata Borbus', field='Social', born=1979, nobel=True),
    Scientist(name='Janna Borbus', field='N/A', born=1979, nobel=True),
    Scientist(name='Vova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='Troy Borbus', field='Happy', born=1979, nobel=True)
}


def transform(x):
    print(f'Processing record {x.name}' + "process running job is : " f'{os.getpid()}')
    time.sleep(1)
    result = {'name': x.name, 'age': 2017 - x.born}
    print(f'Done processing record {x.name}')
    return result


if __name__ == "__main__":
    pprint(scientists)
    start = time.time()
    pool = multiprocessing.Pool()
    result = pool.map(transform, scientists)
    end = time.time()
    print(f'Time to complete: {end - start:.2f}')
    pprint(result)

    print("Now single_process for comparison \n")
    start = time.time()

    mapped_result = tuple(map(
        transform,
        scientists
    ))
    end = time.time()
    print(f'Time to complete: {end - start:.2f}')
    pprint(result)
