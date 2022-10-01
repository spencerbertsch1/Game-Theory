import math

def subtraction_game():
    l = [0,1]  # <-- add list of repeating terms here
    for i in range(101):
        idx = i % len(l)
        print(f'x={i}, g(x)={l[idx]}')

def at_least_half():
    for x in range(1, 101, 1):
        g_x = math.floor(math.log(x, 2)) + 1
        print(f'x={x}, g(x)={g_x}')

def even_if_not_all_all_if_odd():
    for x in range(1, 101, 1):
        if x%2==0:
            g_x = (x/2) - 1
        else:
            g_x = (x+1)/2
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




if __name__ == "__main__":
    # even_if_not_all_all_if_odd()

    print_if_odd(l=[1, 2, 3, 4, 5, 6, 7])
