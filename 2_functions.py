def int_sum(a: int, b: int) -> int:
    return a + b


def int_sub(a: int, b: int) -> int:
    """This function perfoms substraction from of 'b' from 'a'"""
    return a - b


print(type(int_sum))
# print(int_sub.__doc__)
# print(int_sub.__name__)
#
# #set as a var
# f = int_sum
#
# print(f(5, 6))
#
#
# my_list = (int_sum, int_sub)
#
# for f in my_list:
#     print(f(10, 5))
#
#
# #add attr to function
# f = int_sum
# f.some_attr = 'Something'
#
# print(int_sum.some_attr)
# print(dir(int_sum))


def some_func(f: callable, a: int, b: int):
    print(f(a, b))


some_func(int_sum, 10, 5)
some_func(int_sub, 10, 5)
