def positional_args(a, b, c):
    print(f'a={a}, b={b}, c={c}')


positional_args(1, 3, 'some')


#named args

def positional_args(a, b, c: str = None):
    print(f'a={a}, b={b}, c={c}')


positional_args(2, 1, 'some')
positional_args(1, 2, 'some')

# *args, *&kwargs


#def func_args_kwargs(*args):
    #print(f'args={args}')

def func_args_kwargs(**kwargs):
    print(f'kwargs={kwargs}')
    # kwargs.get('some)



#func_args_kwargs(1, 2, 3)
func_args_kwargs(k=123, v='some')


config = {'host': '127.0.0.1', 'port': 6435, 'topic_name': 'something.something'}


def kafka_client(host: str, port: int, topic_name: str):
    print(f'Configured {host}:{port}')


kafka_client(host=config.get('host'), port=config.get('port'), topic_name=config.get('topic_name'))

kafka_client(**config)

my_list = [3, 4, 6]


positional_args(*my_list)
