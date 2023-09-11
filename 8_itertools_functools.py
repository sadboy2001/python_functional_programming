import itertools
import functools

example = [[1, 2, 3, 4], ['some', 'something']]

print(list(itertools.chain(*example)))

print(list(itertools.repeat('abc', 5)))


print(list(itertools.combinations([1, 2, 3, 4], 2)))
print(list(itertools.permutations([1, 2, 3, 4], 2)))


def execute_command_on_server(command: str, host: str, port: int):
    print(f'Execute command "{command}" on server {host}:{port}')


execute_command_on_localhost = functools.partial(execute_command_on_server, host='localhost', port=22)
execute_on_test = functools.partial(execute_command_on_server, host='test.env', port=22)

execute_command_on_localhost('pwd')

from time import sleep
from datetime import datetime


@functools.lru_cache()
def slow_function(a, b):
    sleep(1)
    return a * b


print('Start')
start = datetime.now()

for i in range(5):
    slow_function(1, 2)

print(f'End: {datetime.now() - start}')
