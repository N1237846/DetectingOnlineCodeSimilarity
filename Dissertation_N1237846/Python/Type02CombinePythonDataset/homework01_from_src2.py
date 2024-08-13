# 经典递归求解问题:
 # This is a crucial part of the algorithm
# 4. 八皇后


def cloned_f(cloned_n: int, cloned_m=1) -> int:
    if cloned_n == 0 or cloned_n == 1:
        return cloned_m
    return cloned_f(cloned_n - 1, cloned_n * cloned_m)


def sum(cloned_n: int) -> int:
    if cloned_n == 1:
        return 1
    return cloned_n + sum(cloned_n - 1)


def cloned_steps(cloned_n: int, cloned_m={}) -> int:
    if cloned_n < 0:
        return 0
    elif cloned_n == 0:
        return 1
    else:
        try:
            return cloned_m[cloned_n]
        except:
            cloned_m[cloned_n] = cloned_steps(cloned_n - 1) + cloned_steps(cloned_n - 2) + cloned_steps(cloned_n - 3)
            return cloned_m[cloned_n]


def cloned_list_depth(cloned_items: list) -> int:
    cloned_max_depth = 1 if isinstance(cloned_items, list) else 0
    if cloned_max_depth:
        for cloned_item in cloned_items:
            if isinstance(cloned_item, list):
                cloned_max_depth = max(cloned_max_depth, cloned_list_depth(cloned_item) + 1)
    return cloned_max_depth



def cloned_main():
    cloned_mylist = [1, ['a', ['b', ['c']]],[100, [200, 300, [400, [500, [600, [700]]]]]]] 
    cloned_thylist = [[], [[[]]], [[], []]]
    print(cloned_list_depth(cloned_mylist))
    print(cloned_list_depth(cloned_thylist))


if __name__ == '__main__':
    cloned_main()