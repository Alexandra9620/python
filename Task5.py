from functools import reduce

new_list = [i for i in range(100, 1001) if i % 2 == 0]


def product(prev_el, el):
    return prev_el * el


print(reduce(product, new_list))
