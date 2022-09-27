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

if __name__ == "__main__":
    even_if_not_all_all_if_odd()
