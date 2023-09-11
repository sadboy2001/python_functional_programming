def square(value: int) -> int:
    return value ** 2


def calc_sum(a: int, b: int) -> int:
    return a + b


def main():
    a, b = 2, 3
    my_sum = calc_sum(a, b)
    my_square = square(my_sum)
    print(my_square)
    # print(square(calc_sum(2, 3)))

main()
