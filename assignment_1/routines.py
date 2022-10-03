import math

from nim_player import nim_sum

def subtraction_game(x):
    return x % 2
    # l = [0,1]  # <-- add list of repeating terms here
    # for i in range(101):
    #     idx = i % len(l)
    #     print(f'x={i}, g(x)={l[idx]}')

def at_least_half(x):
    return math.floor(math.log(x, 2)) + 1
    # for x in range(1, 101, 1):
    #     g_x = math.floor(math.log(x, 2)) + 1
    #     print(f'x={x}, g(x)={g_x}')

def even_if_not_all_all_if_odd(x):
    if x%2==0:
        g_x = (x/2) - 1
    else:
        g_x = (x+1)/2
    return g_x
    # for x in range(1, 101, 1):
    #     if x%2==0:
    #         g_x = (x/2) - 1
    #     else:
    #         g_x = (x+1)/2
    #     # print(f'x={x}, g(x)={g_x}')

def multi_game():
    for x in range(1, 101, 1):
        gx_1 = at_least_half(100)
        gx_2 = even_if_not_all_all_if_odd(x)
        gx_3 = subtraction_game(100)
        input_tuple = (int(gx_1), int(gx_2), int(gx_3))
        g_x = nim_sum(input_tuple)
        print(f'x={x}, g(x)={g_x}')

def print_if_odd(l: list) -> list:

    # METHOD #1: use list comprehension to accomplish this goal 
    print([x for x in l if x%2 == 1])

    # METHOD #2: use the filter 
    print(list(filter(lambda x: x%2 == 1, l)))

    # METHOD #3: lazy way 
    odds = []
    for element in l:
        if element%2==1:
            odds.append(element)
    print(odds)

def list_sorting(l: list):
    l.sort(key = lambda x: len(x))
    print(l)

def dict_sorting(d: dict):
    sorted_dict = dict(sorted(d.items(), key = lambda x : len(x[1])))
    print(sorted_dict)

def mean_value_sorting(d: dict):
    sorted_dict = dict(sorted(d.items(), key = lambda x : sum(x[1])/len(x[1])))
    print(sorted_dict)


if __name__ == "__main__":
    multi_game()
