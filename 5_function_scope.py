x = 100


def change_var():
    # print(x)
    x = 5
    print(x)

# def change_var(x):
#     print(id(x))
#     print(x)
#     x += 5
#     print(id(x))
#     print(x)


change_var()
print(x)


def remove_some_numbers(nums: list):
    """
    This functions must filter numbers from nums list that multiple of 3
    """


if __name__ == '__main__':
    example_list = [i for i in range(10)]
    expected_list = [i for i in example_list if i % 3 == 0]
    remove_some_numbers(example_list)
    assert expected_list == example_list, f'Expected \n{expected_list}, got \n{example_list}'