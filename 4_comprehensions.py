integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
integers = [i for i in range(10)]

new_list = []
for i in integers:
    if i % 2 == 0:
        # return i
        new_list.append(i)

new_list = [i for i in integers if i % 2 == 0]
print(list(new_list))

new_g = (i for i in integers if i % 2 == 0)
print(list(new_g))

keys = ['a', 'b', 'c']
values = [1, 2, 3]

key_values = {k: v for k, v in zip(keys, values)}

print(key_values)
